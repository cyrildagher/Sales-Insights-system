type InsightCardProps = {
    title: string
    value: string
    icon?: React.ReactNode
}

export default function InsightCard({ title, value, icon }: InsightCardProps) {
    return (
        <div className="bg-white p-6 rounded-xl shadow-md flex items-center gap-5 border-l-4 border-blue-500 transition-transform hover:scale-105 hover:shadow-lg duration-200">
            {icon && (
                <div className="w-12 h-12 flex items-center justify-center rounded-full bg-blue-100">
                    {icon}
                </div>
            )}
            <div>
                <p className="text-gray-500 text-xs font-medium uppercase tracking-wide mb-1">{title}</p>
                <p className="text-3xl font-bold text-gray-900">{value}</p>
            </div>
        </div>
    )
}