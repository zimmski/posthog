import { InsightModel } from '~/types'
import { dashboardsModel } from '~/models/dashboardsModel'
import { useValues } from 'kea'
import { LemonButton } from 'lib/lemon-ui/LemonButton'
import { IconGauge, IconWithCount } from 'lib/lemon-ui/icons'

interface SaveToDashboardProps {
    insight: Partial<InsightModel>
    setOpenModal: (open: boolean) => void
}

export function AddToDashboard({ insight, setOpenModal }: SaveToDashboardProps): JSX.Element | null {
    const { rawDashboards } = useValues(dashboardsModel)
    const dashboards = insight.dashboard_tiles?.map((tile) => rawDashboards[tile.dashboard_id]).filter((d) => !!d) || []

    if (dashboards.length === 0) {
        return null
    }

    return (
        <span className="save-to-dashboard" data-attr="save-to-dashboard-button">
            <LemonButton
                onClick={() => setOpenModal(true)}
                type="secondary"
                icon={
                    <IconWithCount count={dashboards.length} showZero={false}>
                        <IconGauge />
                    </IconWithCount>
                }
            >
                Edit dashboard(s)
            </LemonButton>
        </span>
    )
}
