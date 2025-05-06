const express=require('express');

const mongoose=require('mongoose');

const app=express();

mongoose.connect('mongodb://127.0.0.1:27017/crudapp')

app.listen(3000, ()=>{
    console.log('Server is running on port 3000');
});
//schema 
const userSchema= new mongoose.Schema({
    name:String,
    email:String,
    address:String, 
    phone:String,
});

app.use(express.json());

const User = mongoose.model('User',userSchema);

//create
app.post('/create',async(req,res)=>{
  const newUser = new User(req.body);
  const savedUser = await newUser.save();  
  res.status(201).json(savedUser);
})
//read
app.get('/read',async(req,res)=>{
  const users = await User.find();
  res.send(users);
});

