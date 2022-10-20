import React, { Component } from "react";

class App extends Component {

    buscardor = document.getElementById('buscar');
    btnBuscar = document.getElementById('buscarBarra');

    constructor() {
        super();
        this.getNews();
        this.state = {
            news: [],
            search: document.getElementById('buscar'),
            script: "Las mejores noticias"
        }
        this.btnBuscar.addEventListener('click', this.buscar);
        this.render();
    }

    buscar = async () => {
        await fetch('/api/search', {
            method: 'POST',
            body: JSON.stringify({ query: this.buscardor.value }),
            headers: {
                "Content-type": "application/json"
            }
        })
            .then(res => res.json())
            .then(data => {
                if(data.length != 0){
                    this.setState({ news: data })
                    this.state.script = "Resultados similares a su búsqueda: " + this.buscardor.value
                }else{
                    this.getNews();
                    this.state.script = "Las mejores noticias";
                    this.buscardor.value = '';
                }
            })
            .catch(err => console.log(err));
        this.render();
    }

    getNews() {
        fetch('/api/news')
            .then(res => res.json())
            .then(data => {
                this.setState({ news: data })
            })
            .catch(err => console.log(err));
    }


    render() {
        return (
            <div>
                <p className="resultado"><span>{this.state.script}</span></p>
                <div className="vitrina">
                    <div className="noticias">
                        {
                            this.state.news.map(notice => (
                                <div className="noticia" key={notice._id} id={notice._id}>
                                    <div className="thumb">
                                        <a href={notice.url} target='_blank'><img src={notice.imagen} alt="noticia" height="250" /></a>
                                    </div>
                                    <div className="informacion">
                                        <h3 className="tituloNoticias"><a href={notice.url} target='_blank'> {notice.titulo} </a></h3>
                                        <p className="fuente"> {notice.fuente} </p>
                                        <p className="categoria"> {notice.categoria} </p>
                                        <p className="fecha"><i className="fa-regular fa-clock"></i> {notice.fecha} </p>
                                    </div>
                                </div>
                            ))
                        }
                    </div>
                </div>
            </div>
        )
    }
}

export default App;