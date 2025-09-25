const mongoose = require('mongoose');

const ItemSchema = new mongoose.Schema({
    name: { type: String, required: true },
    quantity: { type: Number, default: 1 },
    dateAdded: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Item', ItemSchema);
