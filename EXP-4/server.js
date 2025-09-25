const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// MongoDB Atlas Connection
mongoose.connect(
  "mongodb+srv://tanayaitis:<db_password>@cluster0.7ckjy1y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
  {
    useNewUrlParser: true,
    useUnifiedTopology: true
  }
)
.then(() => console.log("✅ MongoDB Atlas Connected"))
.catch(err => console.error("❌ Connection Error:", err));

// Routes
const itemRoutes = require('./routes/items');
app.use('/api/items', itemRoutes);

// Start server
app.listen(5000, () => console.log('🚀 Server running on port 5000'));






// //mongodb local connection
// mongoose.connect("mongodb://127.0.0.1:27017/restapi_demo", {
//     useNewUrlParser: true,
//     useUnifiedTopology: true
// })
// .then(() => console.log("✅ Local MongoDB Connected"))
// .catch(err => console.error("❌ Connection Error:", err));



