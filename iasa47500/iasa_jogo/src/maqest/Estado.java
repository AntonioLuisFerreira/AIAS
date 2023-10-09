package maqest;

import java.util.HashMap;
import java.util.Map;
/**
 *  A classe representa um estado possível da Máquina de Estados de um sistema e é fundamental para caracterizar a dinâmica do mesmo.
 *  Para isso, ela deve conhecer as transições que podem ocorrer a partir deste estado, ou seja, como o sistema age ou reage diante dos estímulos do ambiente.
 *  
 *  Para suportar essa estrutura, a classe é composta por um dicionário que descreve as funções de transformação que ocorrem em resposta aos eventos do ambiente.
 *  Além disso, a classe também possui um nome que é útil para facilitar na impressão e visualização do jogo.
 * 
 *
 * @param <EV> Mapeado com tipo Evento
 * @param <AC> Mapeado com tipo de Accao
 */
public class Estado<EV,AC> {
	
	/** 
	 * Dois Atributos privados,
	 * nome do estado
	 * map das transições
	 * 
	 */
	private String nome;
	private Map<EV, Transicao<EV,AC>> transicoes;
	
	/**
	 * Construtor da classe Estado
	 * incializa as transições
	 * 
	 * @param nome
	 * 
	 * guarda o parametro como atributo
	 */
	public Estado(String nome){
		//iniciar as transições utilizando o HashMap
		transicoes = new HashMap<>();
		//guardar o nome
		this.nome = nome;
		
	}
	
	/**
	 * Método getter do nome
	 * @return nome
	 */
	public String getNome() {
		return nome;
	}
	
	/**
	 * Neste método dado determinado evento que estará a ser pela Personagem percepcionado.
	 * 
     * Retorna a  transição que deve ter realiza no nível da máquina de estados. 
	 * 
	 * @param evento, envento percentido no ambiente(por processar)
	 * @return transição a ser efetuada
	 */
	public Transicao<EV, AC> processar(EV evento) {
		return transicoes.get(evento);
	}
	
	/**
	 * Método transicao em que acrescenta ao HasMap de que a class é formada por uma entrada na chave do evento 
	 * correspondendo-lhe uma nova transição.
	 * 
	 * No caso deste método, consiste na adição de uma transição.
	 * A personagem não tem de realizar acção.
	 * Para evitar a repetição de  código é chamado um método da classe com a mesma função,
	 * mas que recebe ainda a acção que deve ser desempenhada.
	 * Nesse argumento enviar-se-á null.
	 *  
	 * 
	 * @param evento, entrada do HashMap
	 * @param estadoSucessor, próximo estado
	 * @return instância do próprio estado
	 */
	public Estado<EV,AC> transicao(EV evento, Estado<EV,AC> estadoSucessor) {
		return transicao(evento, estadoSucessor, null);
		
	}
	
	/**
	 * Método transicao em que acrescenta ao HasMap de que a class é formada por uma entrada na chave do evento 
	 * correspondendo-lhe uma nova transição.
	 * 
	 * Depois guarda a entrada do evento enviando um objecto da classe Transicao aqui criado com os argumentos fornecidos.
	 * A ação desempenhada pode ser nula.
	 * 
	 * @param evento, entrada do HasMap
	 * @param estadoSucessor, próximo estado
	 * @param accao, ação a ser realizada
	 * @return nstância do próprio estado
	 */
	public Estado<EV,AC> transicao(EV evento, Estado<EV,AC> estadoSucessor, AC accao) {
		transicoes.put(evento, new Transicao<EV,AC>(estadoSucessor, accao));
		return this;
		
	}
}
