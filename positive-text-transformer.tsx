import React, { useState } from 'react';

const PositiveTextTransformer = () => {
  const [inputText, setInputText] = useState('');
  const [transformedText, setTransformedText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [fileContent, setFileContent] = useState(null);
  const [fileName, setFileName] = useState('');

  // Function to transform text to be overwhelmingly positive
  const transformText = (text) => {
    if (!text) return '';
    
    // Replace negative words with positive alternatives
    let positive = text
      // Negative emotions/situations
      .replace(/angry|mad|furious|upset/gi, 'passionate')
      .replace(/sad|unhappy|depressed|down/gi, 'reflective')
      .replace(/worried|anxious|concerned/gi, 'thoughtful')
      .replace(/problems|issues|troubles/gi, 'opportunities')
      .replace(/difficult|hard|challenging/gi, 'growth-oriented')
      .replace(/failure|failed|failing/gi, 'learning experience')
      .replace(/criticism|critique/gi, 'feedback')
      .replace(/complaint|complaining/gi, 'suggestion')
      .replace(/mistake|error/gi, 'growth opportunity')
      .replace(/terrible|awful|horrible/gi, 'presenting unique opportunities')
      .replace(/hate|dislike/gi, 'have opportunities to appreciate')
      .replace(/bad|poor/gi, 'developing')
      .replace(/wrong/gi, 'different perspective')
      .replace(/can't|cannot|couldn't/gi, 'haven\'t yet')
      .replace(/won't|will not/gi, 'may choose to')
      .replace(/fear|afraid/gi, 'anticipate')
      .replace(/annoyed|annoying/gi, 'intrigued')
      .replace(/unfortunately/gi, 'interestingly')
      .replace(/never/gi, 'not yet')
      
      // Modifying negative sentence structures
      .replace(/isn't|is not/gi, 'has the potential to be')
      .replace(/aren't|are not/gi, 'have the opportunity to be')
      .replace(/don't|do not/gi, 'have the chance to')
      .replace(/shouldn't|should not/gi, 'might consider')
      
      // Add positive reinforcement to sentences that might still sound negative
      .replace(/\./gi, '. 💖 ')
      .replace(/\!/gi, '! ✨ ')
      .replace(/\?/gi, '? 🌈 ');
    
    // Add timestamp
    const now = new Date();
    const timestamp = now.toLocaleString();
    positive += `\n\n[Positively transformed on ${timestamp}] 🌈✨💖`;
    
    return positive;
  };

  const handleTransform = () => {
    setIsLoading(true);
    
    // Use setTimeout to give a sense of processing
    setTimeout(() => {
      const positive = transformText(inputText || fileContent);
      setTransformedText(positive);
      setIsLoading(false);
    }, 1000);
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setFileName(file.name);
      const reader = new FileReader();
      reader.onload = (e) => {
        setFileContent(e.target.result);
        setInputText(''); // Clear direct input when file is loaded
      };
      reader.readAsText(file);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(transformedText);
    alert('Positive text copied to clipboard! 🎉');
  };

  const handleClear = () => {
    setInputText('');
    setTransformedText('');
    setFileContent(null);
    setFileName('');
  };

  return (
    <div className="p-6 max-w-4xl mx-auto bg-gradient-to-r from-pink-100 to-blue-100 rounded-lg shadow-lg">
      <div className="text-center mb-6">
        <h1 className="text-3xl font-bold text-pink-600 mb-2">Ultimate Care Bear (UCB)</h1>
        <p className="text-lg text-blue-600">Transform any text into pure positive vibes! ✨</p>
      </div>
      
      <div className="mb-6">
        <div className="flex flex-col mb-4">
          <label className="mb-2 text-lg font-medium text-purple-600">Enter text to transform:</label>
          <textarea 
            className="p-4 border-2 border-pink-300 rounded-lg focus:border-pink-500 focus:ring focus:ring-pink-200 transition"
            rows="6"
            placeholder="Paste your text here..."
            value={inputText}
            onChange={(e) => {
              setInputText(e.target.value);
              setFileContent(null);
              setFileName('');
            }}
          />
        </div>
        
        <div className="mb-4">
          <p className="mb-2 text-lg font-medium text-purple-600">Or upload a file:</p>
          <div className="flex items-center">
            <input
              type="file"
              onChange={handleFileChange}
              className="hidden"
              id="file-upload"
              accept=".txt,.doc,.docx,.pdf,.md"
            />
            <label 
              htmlFor="file-upload" 
              className="px-4 py-2 bg-blue-500 text-white rounded-lg cursor-pointer hover:bg-blue-600 transition"
            >
              Choose File
            </label>
            {fileName && (
              <span className="ml-4 text-blue-600">{fileName}</span>
            )}
          </div>
        </div>
        
        <div className="flex space-x-4">
          <button 
            onClick={handleTransform}
            disabled={isLoading || (!inputText && !fileContent)}
            className={`px-6 py-2 rounded-lg font-medium text-white transition ${(!inputText && !fileContent) || isLoading ? 'bg-gray-400' : 'bg-pink-500 hover:bg-pink-600'}`}
          >
            {isLoading ? 'Spreading Positivity...' : 'Transform! 🌈'}
          </button>
          
          <button 
            onClick={handleClear}
            className="px-6 py-2 bg-purple-500 text-white rounded-lg font-medium hover:bg-purple-600 transition"
          >
            Clear All
          </button>
        </div>
      </div>
      
      {transformedText && (
        <div className="mt-8">
          <div className="flex justify-between items-center mb-2">
            <h2 className="text-xl font-medium text-green-600">Positively Transformed Text:</h2>
            <button 
              onClick={handleCopy}
              className="px-4 py-1 bg-green-500 text-white rounded-lg text-sm hover:bg-green-600 transition"
            >
              Copy Text
            </button>
          </div>
          <div className="p-4 bg-white border-2 border-green-300 rounded-lg whitespace-pre-wrap">
            {transformedText}
          </div>
        </div>
      )}
    </div>
  );
};

export default PositiveTextTransformer;