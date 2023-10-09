package jogo.personagem;

import jogo.ambiente.Ambiente;

/**
 * A classe Personagem permite fabricar um comportamento da personagem com relação ao seu meio.
 * É composta pela classe Controlo e pela classe Ambiente
 * 
 * 
 * @author amvlf
 *
 */
public class Personagem {

	/**
	 * Dois atributos privados
	 * controlo que faz a referência para o objecto Controlo, e cria um objecto da classe Controlo
	 * ambiente que faz a referência para o objecto Ambiente
	 */
	
	private Controlo controlo = new Controlo();
	private Ambiente ambiente;
	
	
	/**
	 * É o construtor do ambiente 
	 * 
	 * 
	 * @param ambiente
	 * guarda o ambiente como atributo
	 */
	public Personagem(Ambiente ambiente) {
		this.ambiente = ambiente;
	}
	
	/**
	 * Permite à personagem ter noção do que a rodeia.
	 * 
	 * @return percepcao
	 */
	public Percepcao percepcionar() {
		return new Percepcao(ambiente.getEvento());
	}
	
	/**
	 * Recebe uma ação, e dá print da consola da ação escolhida
	 * 
	 * @param accao
	 */
	public void actuar(Accao accao) {
		if(accao != null) {
			System.out.println("Ação => " + accao.toString());
		}
	}
	
	/**
	 * Método chamado pelo main da aplicação que permite à personagem executar as suas ações
	 */
	public void executar() {
		actuar(controlo.processar(percepcionar()));
	}
}
