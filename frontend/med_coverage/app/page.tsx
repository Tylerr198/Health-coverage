"use client";
import { useState } from "react";
import axios from "axios";

export default function Home() {

    const [prompt, setPrompt] = useState({
      ask: ""
    })

    const [response, setResponse] = useState("")

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const {value} = event.target;
        setPrompt(() => ({
          ask: value
        }))
    }
    
    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
      event.preventDefault();
      console.log("Prompt submitted:", prompt )
      try {
        const response = await axios.post('http://127.0.0.1:5000/ask', {prompt})
        setResponse(response.data.message)
      } catch (error) {
        console.log("Error:", error)
      };
      
      setPrompt({ask:""});
    }



  return (
    <main className="h-screen w-screen">
        <h1 className="text-center text-2xl my-2">Med Assist</h1>
        <div className="w-3/4 h-1/4 bg-nice_blue mx-auto text-2xl">
          Hey this is Med Assist 👋. Designed to help you better understand
          your health coverage in an easy and accessible way.
        </div>
        <form className="flex justify-center my-2" onSubmit={handleSubmit}>
          <input className="border-black border-1" placeholder="Ask a question!" value={prompt.ask} onChange={handleChange}/>
          <button type="submit" className="bg-darker_blue rounded-md text-white p-1">Submit</button>
        </form>
        <div className="w-1/2 h-1/4 mx-auto my-4 bg-nice_yellow font-medium justify-center flex p-3">{response}</div>
    </main>
  );
}
