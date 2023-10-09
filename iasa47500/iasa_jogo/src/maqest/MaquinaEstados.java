package maqest;

/**
 * A classe MaquinaEstados é responsável por gerenciar as transições entre estados,
 * permitindo que a personagem evolua em resposta aos eventos que ocorrem no ambiente do jogo.
 * Esse processo segue o Modelo Formal de Computação, utilizando uma Máquina de Estados do tipo de Mealy,
 * onde a função de saída depende das entradas.
 * 
 * Para isso, a classe MaquinaEstados utiliza os enumerados Evento e Accao, que representam, respectivamente,
 * o alfabeto de entrada e de saída.
 * No entanto, a biblioteca deve ser flexível e permitir o uso de outros tipos de eventos e respostas,
 * por isso, são utilizados genéricos EV (Mapeado com tipo Evento) e AC (Mapeado com tipo de Accao).
 * 
 * @param <EV> Mapeado com tipo Evento
 * @param <AC> Mapeado com tipo de Accao
 */

public class MaquinaEstados <EV,AC> {

	//atributo privado que aponta para a classe Estado
	private Estado <EV, AC> estado;
		
	/**
	 * Construtor da classe MaquinaEstados
	 * 
	 * @param estado
	 * guardando o parametro em memória
	 */
	public MaquinaEstados(Estado <EV, AC> estado) {
		this.estado = estado;
	}
	
	/**
	 * Método getter do estado	
	 * @return estado
	 */
	public Estado <EV, AC> getEstado() {
		return estado;
	}
	
	/**
	 * O método Processar, face a um evento que ocorre no Ambiente, permite 
     * interpretar de acordo com o estado atual, e atualizando o seu estado,
     * passanado para estado sucessor, retornando ainda a ação necessária.
     * 
	 * @param evento
	 * @return transicao.getAccao
	 * @return null ,em caso de a transicao ser nula
	 */
	public AC processar(EV evento) {
		Transicao<EV, AC> transicao = estado.processar(evento);
        if (transicao != null){
            estado = transicao.getEstadoSucessor();
            AC accao = transicao.getAccao();
            return accao;
        } 
        return null;
	}
	
}
