import { Link, LemonButton } from '@posthog/lemon-ui'
import { useActions, useValues } from 'kea'
import { LemonMenuItem, LemonMenu } from 'lib/lemon-ui/LemonMenu'
import { IconLink, IconCheckmark, IconCloudDownload, IconSettings, IconEllipsis, IconLegend } from 'lib/lemon-ui/icons'
import { PluginImage } from 'scenes/plugins/plugin/PluginImage'
import { SuccessRateBadge } from 'scenes/plugins/plugin/SuccessRateBadge'
import { pluginsLogic } from 'scenes/plugins/pluginsLogic'
import { PluginTypeWithConfig, PluginRepositoryEntry, PluginInstallationType } from 'scenes/plugins/types'
import { urls } from 'scenes/urls'
import { PluginType } from '~/types'
import { PluginTags } from './components'

export function AppView({
    plugin,
}: {
    plugin: PluginTypeWithConfig | PluginType | PluginRepositoryEntry
}): JSX.Element {
    const { installingPluginUrl, pluginsNeedingUpdates, pluginsUpdating, showAppMetricsForPlugin, loading } =
        useValues(pluginsLogic)
    const { installPlugin, editPlugin, toggleEnabled, updatePlugin } = useActions(pluginsLogic)

    const pluginConfig = 'pluginConfig' in plugin ? plugin.pluginConfig : null
    const isConfigured = !!pluginConfig?.id
    const menuItems: LemonMenuItem[] = []

    if (plugin.url) {
        menuItems.push({
            label: 'Source',
            sideIcon: <IconLink />,
            to: plugin.url,
            targetBlank: true,
        })
    }

    if (isConfigured) {
        menuItems.push({
            label: pluginConfig?.enabled ? 'Disable' : 'Enable',
            status: pluginConfig.enabled ? 'danger' : 'primary',
            onClick: () =>
                toggleEnabled({
                    id: pluginConfig.id,
                    enabled: !pluginConfig.enabled,
                }),
        })
    }

    return (
        <div className="flex justify-between items-center">
            <div className="flex items-center gap-4">
                <PluginImage plugin={plugin} />
                <div>
                    <div className="flex gap-2 items-center">
                        {pluginConfig && showAppMetricsForPlugin(plugin) && pluginConfig.id && (
                            <SuccessRateBadge
                                deliveryRate={pluginConfig.delivery_rate_24h ?? null}
                                pluginConfigId={pluginConfig.id}
                            />
                        )}
                        <span className="font-semibold truncate">
                            {isConfigured ? (
                                <Link
                                    to={isConfigured ? urls.appMetrics(pluginConfig.id || '') : plugin.url}
                                    target={!isConfigured ? 'blank' : undefined}
                                >
                                    {plugin.name}
                                </Link>
                            ) : (
                                plugin.name
                            )}
                        </span>
                        <PluginTags plugin={plugin} />
                    </div>
                    <div className="text-sm">{plugin.description}</div>
                </div>
            </div>

            <div className="flex gap-2 whitespace-nowrap items-center justify-end">
                {'id' in plugin && pluginConfig ? (
                    <>
                        {!pluginConfig.enabled && isConfigured && (
                            <LemonButton
                                type="secondary"
                                size="small"
                                onClick={() =>
                                    toggleEnabled({
                                        id: pluginConfig.id,
                                        enabled: true,
                                    })
                                }
                            >
                                Enable
                            </LemonButton>
                        )}

                        {'updateStatus' in plugin && pluginsNeedingUpdates.find((x) => x.id === plugin.id) && (
                            <LemonButton
                                type="secondary"
                                size="small"
                                onClick={() => {
                                    plugin.updateStatus?.updated ? editPlugin(plugin.id) : updatePlugin(plugin.id)
                                }}
                                loading={pluginsUpdating.includes(plugin.id)}
                                icon={plugin.updateStatus?.updated ? <IconCheckmark /> : <IconCloudDownload />}
                            >
                                {plugin.updateStatus?.updated ? 'Updated' : 'Update'}
                            </LemonButton>
                        )}

                        {pluginConfig.id && (
                            <LemonButton
                                type="secondary"
                                size="small"
                                icon={<IconLegend />}
                                to={urls.appLogs(pluginConfig.id)}
                            >
                                Logs & metrics
                            </LemonButton>
                        )}

                        <LemonButton
                            type="primary"
                            size="small"
                            icon={<IconSettings />}
                            onClick={() => editPlugin(plugin.id)}
                        >
                            Configure
                        </LemonButton>
                    </>
                ) : (
                    <LemonButton
                        type="primary"
                        loading={loading && installingPluginUrl === plugin.url}
                        icon={<IconCloudDownload />}
                        size="small"
                        onClick={() =>
                            plugin.url ? installPlugin(plugin.url, PluginInstallationType.Repository) : undefined
                        }
                    >
                        Install
                    </LemonButton>
                )}

                <LemonMenu items={menuItems} placement="left">
                    <LemonButton size="small" icon={<IconEllipsis />} />
                </LemonMenu>
            </div>
        </div>
    )
}
