package jogo.personagem;

import jogo.ambiente.Evento;

/**
 * A classes das quais a classe Controlo depende.
 * 
 * Percepção permitirá armazenar o evento que decorre atualmente,armazenando como atributo,
 * para que para depois possa interpretado pela personagem.
 * Em suma guarda a noção de personagem ao seu meio envolvente.
 * 
 * @author amvlf
 *
 */

public class Percepcao {
	
	/**
	 * Atributo privado
	 * evento que faz a referência para o objecto Evento
	 */
	private Evento evento;
	
	 /**
     * É o construtor da classe.
     * 
     * @params evento
     * guarda o evento como atributo
     */
	public Percepcao(Evento evento) {
		this.evento = evento;
	}
	
	/**
	 * Retorna o atributo evento.
	 *  
	 * @return evento
	 */
	public Evento getEvento() {
		return evento;
	}
}
