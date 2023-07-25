import { useMemo } from 'react'
import { useActions, useMountedLogic, useValues } from 'kea'
import { propertyFilterLogic } from 'lib/components/PropertyFilters/propertyFilterLogic'
import { taxonomicPropertyFilterLogic } from './taxonomicPropertyFilterLogic'
import { PropertyKeyInfo } from 'lib/components/PropertyKeyInfo'
import { OperatorValueSelect } from 'lib/components/PropertyFilters/components/OperatorValueSelect'
import { isOperatorMulti, isOperatorRegex } from 'lib/utils'
import { TaxonomicFilter } from 'lib/components/TaxonomicFilter/TaxonomicFilter'
import {
    TaxonomicFilterGroup,
    TaxonomicFilterGroupType,
    TaxonomicFilterValue,
} from 'lib/components/TaxonomicFilter/types'
import {
    isGroupPropertyFilter,
    isPropertyFilterWithOperator,
    propertyFilterTypeToTaxonomicFilterType,
} from 'lib/components/PropertyFilters/utils'
import { PropertyFilterInternalProps } from 'lib/components/PropertyFilters/types'
import { propertyDefinitionsModel } from '~/models/propertyDefinitionsModel'
import { AnyPropertyFilter, FilterLogicalOperator, PropertyDefinitionType, PropertyFilterType } from '~/types'
import { LemonButton } from '@posthog/lemon-ui'
import { LemonDropdown } from 'lib/lemon-ui/LemonDropdown'
import { IconSubdirectoryArrowRight } from 'lib/lemon-ui/icons'

let uniqueMemoizedIndex = 0

export function TaxonomicPropertyFilter({
    pageKey: pageKeyInput,
    index,
    onComplete,
    disablePopover, // inside a dropdown if this is false
    taxonomicGroupTypes,
    eventNames,
    propertyGroupType,
    orFiltering,
    addButton,
    hasRowOperator,
}: PropertyFilterInternalProps): JSX.Element {
    const pageKey = useMemo(() => pageKeyInput || `filter-${uniqueMemoizedIndex++}`, [pageKeyInput])
    const groupTypes = taxonomicGroupTypes || [
        TaxonomicFilterGroupType.EventProperties,
        TaxonomicFilterGroupType.PersonProperties,
        TaxonomicFilterGroupType.EventFeatureFlags,
        TaxonomicFilterGroupType.Cohorts,
        TaxonomicFilterGroupType.Elements,
        TaxonomicFilterGroupType.HogQLExpression,
    ]
    const taxonomicOnChange: (group: TaxonomicFilterGroup, value: TaxonomicFilterValue, item: any) => void = (
        taxonomicGroup,
        value
    ) => {
        selectItem(taxonomicGroup, value)
        if (
            taxonomicGroup.type === TaxonomicFilterGroupType.Cohorts ||
            taxonomicGroup.type === TaxonomicFilterGroupType.HogQLExpression
        ) {
            onComplete?.()
        }
    }
    const builtPropertyFilterLogic = useMountedLogic(propertyFilterLogic)
    const { setFilter } = useActions(propertyFilterLogic)

    const logic = taxonomicPropertyFilterLogic({
        pageKey,
        propertyFilterLogic: builtPropertyFilterLogic,
        filterIndex: index,
        taxonomicGroupTypes: groupTypes,
        taxonomicOnChange,
        eventNames,
    })
    const { filter, dropdownOpen, selectedCohortName, activeTaxonomicGroup } = useValues(logic)
    const { openDropdown, closeDropdown, selectItem } = useActions(logic)
    const showInitialSearchInline =
        !disablePopover &&
        ((!filter?.type && (!filter || !(filter as any)?.key)) ||
            filter?.type === PropertyFilterType.Cohort ||
            filter?.type === PropertyFilterType.HogQL)
    const showOperatorValueSelect =
        filter?.type &&
        filter?.key &&
        filter?.type !== PropertyFilterType.Cohort &&
        filter?.type !== PropertyFilterType.HogQL

    const { propertyDefinitionsByType } = useValues(propertyDefinitionsModel)

    // We don't support array filter values here. Multiple-cohort only supported in TaxonomicBreakdownFilter.
    // This is mostly to make TypeScript happy.
    const cohortOrOtherValue =
        filter?.type === 'cohort' ? (!Array.isArray(filter?.value) && filter?.value) || undefined : filter?.key

    const taxonomicFilter = (
        <TaxonomicFilter
            groupType={propertyFilterTypeToTaxonomicFilterType(
                filter?.type,
                isGroupPropertyFilter(filter) ? filter.group_type_index : undefined
            )}
            value={cohortOrOtherValue}
            onChange={taxonomicOnChange}
            taxonomicGroupTypes={groupTypes}
            eventNames={eventNames}
        />
    )

    return showInitialSearchInline ? (
        taxonomicFilter
    ) : (
        <div className="flex gap-2 overflow-hidden">
            {hasRowOperator && (
                <div className="flex justify-end items-center shrink-0 h-10">
                    {orFiltering ? (
                        <>
                            {propertyGroupType && index !== 0 && filter?.key && (
                                <div className="text-sm font-medium">
                                    {propertyGroupType === FilterLogicalOperator.And ? '&' : propertyGroupType}
                                </div>
                            )}
                        </>
                    ) : (
                        <div className="flex items-center gap-2">
                            {index === 0 ? (
                                <>
                                    <IconSubdirectoryArrowRight className="text-xl text-border-bold" />
                                    <span>where</span>
                                </>
                            ) : (
                                <span className="stateful-badge and text-xs">AND</span>
                            )}
                        </div>
                    )}
                </div>
            )}
            <div className="flex flex-auto flex-wrap items-start gap-2 overflow-hidden">
                <LemonDropdown
                    overlay={dropdownOpen ? taxonomicFilter : null}
                    visible={dropdownOpen}
                    placement="bottom"
                    onClickOutside={() => closeDropdown()}
                >
                    <LemonButton
                        status="stealth"
                        onClick={() => (dropdownOpen ? closeDropdown() : openDropdown())}
                        type="secondary"
                        sideIcon={addButton ? null : undefined}
                        data-attr={'property-select-toggle-' + index}
                    >
                        {filter?.type === 'cohort' ? (
                            <div>{selectedCohortName || `Cohort #${filter?.value}`}</div>
                        ) : filter?.key ? (
                            <PropertyKeyInfo value={filter.key} disablePopover ellipsis />
                        ) : (
                            <>{addButton || <div>Add filter</div>}</>
                        )}
                    </LemonButton>
                </LemonDropdown>
                {showOperatorValueSelect ? (
                    <OperatorValueSelect
                        propertyDefinitions={propertyDefinitionsByType(filter?.type || PropertyDefinitionType.Event)}
                        type={filter?.type}
                        propkey={filter?.key}
                        operator={isPropertyFilterWithOperator(filter) ? filter.operator : null}
                        value={filter?.value}
                        placeholder="Enter value..."
                        endpoint={filter?.key && activeTaxonomicGroup?.valuesEndpoint?.(filter.key)}
                        eventNames={eventNames}
                        onChange={(newOperator, newValue) => {
                            if (filter?.key && filter?.type) {
                                setFilter(index, {
                                    key: filter?.key,
                                    value: newValue || null,
                                    operator: newOperator,
                                    type: filter?.type,
                                    ...(isGroupPropertyFilter(filter)
                                        ? { group_type_index: filter.group_type_index }
                                        : {}),
                                } as AnyPropertyFilter)
                            }
                            if (
                                newOperator &&
                                newValue &&
                                !isOperatorMulti(newOperator) &&
                                !isOperatorRegex(newOperator)
                            ) {
                                onComplete()
                            }
                        }}
                    />
                ) : (
                    <div />
                )}
            </div>
        </div>
    )
}
