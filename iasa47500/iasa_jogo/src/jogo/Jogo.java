package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/**
 * A classe Jogo é formada por uma instância da classe Ambiente e outra da classe Personagem.
 * O seu propósito é fornecer a base para a execução do jogo.
 * Ao inicializar as instâncias de Ambiente e Personagem que permitem o funcionamento do jogo.
 * Para além disso, a classe Jogo trata todas as chamadas necessárias para a execução e progressão do jogo.
 */
public class Jogo {
	
	/**
	 * Dois atributos privados,
	 * 
	 * 1º personagem que faz a referência para o objecto Personagem
	 * 
	 * 2º ambiente que faz a referência para o objecto Ambiente
	 */
	private static Personagem personagem;
	private static Ambiente ambiente;
		
	/**
	 * O método permite realizar o comportamento do Jogo,
	 * até terminar
	 *
	 */
	private static void executar() {
		/**
		 * do-while, pois é necessário uma primeira execução antes de terminar
		 */
		do {
			personagem.executar();
			ambiente.evoluir();
		} while (ambiente.getEvento() != Evento.TERMINAR);
	}
		
	/**
	 * Main é o método responsável por tratar a inicialização dos atributos
	 * 
	 * @param args não é usado
	 */
	public static void main(String[] args) {
		ambiente   = new Ambiente();
		personagem = new Personagem(ambiente);
		executar();
	}

}
