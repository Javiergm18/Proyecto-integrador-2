import React, { Component } from "react";

class App extends Component {

    buscardor = document.getElementById('buscar');
    btnBuscar = document.getElementById('buscarBarra');

    constructor() {
        super();
        this.getNews();
        this.state = {
            news: [],
            search: document.getElementById('buscar')
        }
        this.btnBuscar.addEventListener('click', this.buscar);
        this.render();
        // this.addUrl();
    }

    addUrl() {
        alert('prueba');
        console.log('prueba');
        this.state.news.map(notice => {
            let id = notice._id;
            let temp = document.getElementById(id);
            let url = notice.url;
            temp.addEventListener('click', () => {
                alert('prueba');
                window.open(url, '_blank');
            })
        })
    }

    buscar = () => {
        console.log(this.buscardor.value);
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
                <p className="resultado"><span>Las mejores noticias</span></p>
                <div className="vitrina">
                    <div className="noticias">
                        {
                            this.state.news.map(notice => (
                                <div className="noticia" key={notice._id} id={notice._id}>
                                    <div className="thumb">
                                        <a href={notice.url} target='_blank'><img src={notice.imagen} alt="noticia" height="250"/></a>
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