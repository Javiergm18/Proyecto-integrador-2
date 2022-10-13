const { json } = require('express');
const express = require('express');
const news = require('../models/news');
const router = express.Router();

const fechaDate = new Date();
let mes = fechaDate.getMonth() + 1;
if(mes < 10){
    mes = '0' + String(mes)
}
let dia = fechaDate.getDate();
if(dia < 10){
    dia = '0' + String(dia);
}

const fechaHoy = fechaDate.getFullYear() +"-"+ mes + "-" + dia;

const Notice = require('../models/news');

router.get('/', async (req, res) => {
    const news = await Notice.find({fecha: fechaHoy});
    if(news.length === 0){
        let fechaAyer = calculateDate();
        let news2 = await Notice.find({fecha: fechaAyer});
        res.json(news2);
    }else{
        res.json(news);
    }
});

function calculateDate(){
    let fechaTemp = new Date();
    fechaTemp.setDate(fechaDate.getDate()-1);
    let mes = fechaTemp.getMonth() + 1;
    if(mes < 10){
        mes = '0' + String(mes)
    }
    let fechaAyer = fechaTemp.getFullYear() +"-"+ mes + "-" +fechaTemp.getDate();
    return fechaAyer;
}

module.exports = router;