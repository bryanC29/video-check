interface UploadBoxProps {
  setVideo: (file: File) => void
  setResult: (result: AnalysisResult) => void
}

interface AnalysisResult {
  filename: string
  tampered: boolean
  hash: string
  metadataValid: boolean
  analysis: string
}

export default function UploadBox({ setVideo, setResult }: UploadBoxProps) {
  const handleFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      setVideo(file)

      // Simulate analysis
      setTimeout(() => {
        setResult({
          filename: file.name,
          tampered: false,
          hash: 'a1b2c3d46s5v4d35vv4dv5dvdaqd8csv38t4brb51684vs',
          metadataValid: true,
          analysis: 'No signs of tampering detected.'
        })
      }, 1500)
    }
  }

  return (
    <div className="bg-blue-400 p-6 rounded-xl shadow-md ">
      <label
        htmlFor="upload"
        className="block border-2 border-dashed border-gray-300 p-6 text-center rounded-md cursor-pointer hover:border-black"
      >
        <p className="text-indigo-900 font-semibold">Click to upload or drag here</p>
        <p className="text-sm text-gray-600 mt-1">Supports: MP4, MOV</p>
      </label>
      <input
        id="upload"
        type="file"
        accept="video/mp4,video/mov"
        onChange={handleFile}
        className="hidden"
      />
    </div>
  )
}
