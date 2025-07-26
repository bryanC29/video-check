// import { AnalysisResult } from './types'

interface HistoryListProps {
    history: AnalysisResult[]
}

interface AnalysisResult {
    filename: string
    tampered: boolean
    hash: string
    metadataValid: boolean
    analysis: string
}

export default function HistoryList({ history }: HistoryListProps) {
    return (
        <div className="bg-gray-300 p-4 rounded-xl shadow-md mt-4">
            {/* <h2 className="text-lg font-semibold mb-3 text-black">📜 Upload History</h2> */}
            {history.length === 0 ? (
                <p className="text-black m-2">No uploads yet.</p>
            ) : (
                <ul className="space-y-2">
                    {history.map((item, idx) => (
                        <li key={idx} className="border-b py-2">
                            <div className="flex justify-between">
                                <span className="text-black">{item.filename}</span>
                                <span className={item.tampered ? "text-red-600" : "text-green-600"}>
                                    {item.tampered ? "Tampered" : "Approved"}
                                </span>
                            </div>
                            <p className="text-sm text-neutral-700">Hash: {item.hash}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    )
}
