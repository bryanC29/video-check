import React, { useEffect, useRef, useState } from 'react'

interface AnalysisResult {
    filename: string
    tampered: boolean
    hash: string
    metadataValid: boolean
    analysis: string
}

interface Props {
    result: AnalysisResult
    videoFile: File | null
}

export default function ResultCard({ result, videoFile }: Props) {
    const videoRef = useRef<HTMLVideoElement>(null)
    const canvasRef = useRef<HTMLCanvasElement>(null)
    const [thumbnailURL, setThumbnailURL] = useState<string | null>(null)

    useEffect(() => {
        if (!videoFile) return

        const videoURL = URL.createObjectURL(videoFile)
        const video = document.createElement('video')
        video.src = videoURL
        video.crossOrigin = 'anonymous'
        video.preload = 'metadata'

        video.onloadeddata = () => {
            video.currentTime = 1
        }

        video.onseeked = () => {
            const canvas = document.createElement('canvas')
            canvas.width = video.videoWidth
            canvas.height = video.videoHeight
            const ctx = canvas.getContext('2d')
            if (ctx) {
                ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
                const imgURL = canvas.toDataURL()
                setThumbnailURL(imgURL)
            }
            URL.revokeObjectURL(videoURL)
        }
    }, [videoFile])

    return (
        <div className="bg-white shadow-md rounded-xl p-6 mt-6 flex flex-col lg:flex-row gap-6">
            {/* Left: Thumbnail Image */}
            <div className="w-full lg:w-1/2 flex justify-center items-center">
                {thumbnailURL ? (
                    <img
                        src={thumbnailURL}
                        alt="Video Thumbnail"
                        className="rounded-lg w-full max-h-64 object-cover"
                    />
                ) : (
                    <div className="text-gray-500 text-center">Generating thumbnail...</div>
                )}
            </div>

            {/* Right: Analysis Info */}
            <div className="w-full lg:w-1/2 space-y-3 text-sm text-gray-800">
                <h2 className="text-xl font-bold mb-2">Analysis Result</h2>

                <div className="flex justify-between border-b pb-2">
                    <span className="font-medium">Filename:</span>
                    <span className="text-gray-600 font-bold">{result.filename}</span>
                </div>

                <div className="flex justify-between border-b pb-2">
                    <span className="font-medium">Status:</span>
                    <span className={result.tampered ? "text-red-700 font-bold" : "text-green-700 font-bold"}>
                        {result.tampered ? "Tampered" : "Clean"}
                    </span>
                </div>

                <div className="flex justify-between border-b pb-2">
                    <span className="font-medium">Metadata:</span>
                    <span className={result.metadataValid ? "text-green-700 font-bold" : "text-red-700 font-bold"}>
                        {result.metadataValid ? "Valid" : "Invalid"}
                    </span>
                </div>

                <div className="border-b pb-2">
                    <span className="font-medium block">Hash:</span>
                    <div className="text-medium text-gray-600 bg-gray-200 px-2 py-1 rounded break-all mt-1">
                        {result.hash}
                    </div>
                </div>

                <div className='border-b'>
                    <span className="font-medium block ">Detailed Analysis:</span>
                    <p className="text-gray-700 mt-1 whitespace-pre-line mb-2">{result.analysis}</p>
                </div>
            </div>
        </div>
    )
}
