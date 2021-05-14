// const start = callback => {
//   setTimeout(() => {
//     callback('Hello');
//     setTimeout(() => {
//       callback('And Welcome');
//       setTimeout(() => {
//         callback('To Async Await Using TypeScript');
//       }, 1000);
//     }, 1000);
//   }, 1000);
// };
// start(text => console.log(text));

async function myfunction():Promise<string>{
    const rankPromise = getRank()
    const rank = await rankPromise;
    return "hero number" + rank;
    
    console.log("getting")
}

function getRank(){
    return Promise.resolve(1);
}
