

export default function Home() {
  return (
    <main className="h-screen w-screen">
        <h1 className="text-center text-2xl my-2">Med Assist</h1>
        <div className="w-3/4 h-1/4 bg-nice_blue mx-auto text-2xl">
          Hey this is Med Assist 👋. Designed to help you better understand
          your health coverage in an easy and accessible way.
        </div>
        <div className="flex justify-center my-2">
          <input className="border-black border-1" placeholder="Ask a question!"/> 
          <button type="submit" className="bg-darker_blue rounded-md text-white p-1">Submit</button>
        </div>
        <div className="w-1/2 h-1/4 mx-auto my-4 bg-nice_yellow font-medium justify-center flex p-3">Lorem ipsum dolor sit amet consectetur adipisicing elit. Distinctio excepturi aliquid necessitatibus obcaecati iste illo adipisci mollitia blanditiis eius voluptate facere, et quia nam possimus. Natus odit quae explicabo ea!</div>
    </main>
  );
}
