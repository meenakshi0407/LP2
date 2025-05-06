const express=require('express');

const app=express();

app.use(express.static('public'));

app.listen(3000, ()=>{
    console.log('Hello, this is first time creating node.js server!')
})

