"use client"
import Header from '@/components/Header'
import UploadBox from '@/components/UploadBox'
import ResultCard from '@/components/ResultCard'
import HistoryList from '@/components/HistoryList'
import { useState } from 'react'

interface AnalysisResult {
  filename: string
  tampered: boolean
  hash: string
  metadataValid: boolean
  analysis: string
}

function App() {
  const [video, setVideo] = useState<File | null>(null)
  const [result, setResult] = useState<AnalysisResult | null>(null)
  const [history, setHistory] = useState<AnalysisResult[]>([])

  const handleResult = (newResult: AnalysisResult) => {
    setResult(newResult)
    setHistory(prev => [newResult, ...prev])
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />

      <div className="flex flex-col lg:flex-row gap-6 px-4 py-10">
        {/* Main Section */}
        <main className="flex-1">
          <UploadBox setVideo={setVideo} setResult={handleResult} />
          {result && <ResultCard result={result} videoFile={video} />}
        </main>

        {/* History Section */}
        <aside className="w-full lg:w-1/3">
          <div className="bg-white rounded-xl shadow-md p-4">
            <h2 className="text-lg text-black font-semibold mb-4">History</h2>
            <HistoryList history={history} />
          </div>
        </aside>
      </div>
    </div>

  )
}

export default App
