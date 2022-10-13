const mongoose = require('mongoose');
const { Schema } = mongoose;

const noticeSchema = new Schema({
    imagen: {type: String, required: true},
    titulo: {type: String, required: true},
    url: {type: String, required: true},
    categoria: {type: String, required: true},
    fecha: {type: String, required: true},
    fuente: {type: String, required: true}
});

module.exports = mongoose.model('noticias', noticeSchema);