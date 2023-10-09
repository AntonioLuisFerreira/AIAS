package jogo.personagem;

/**
 * Enumeração das ações que podem ser utilizadas
 * 
 */
public enum Accao {
	
	/**
	 * Procurar é o estado inicial, pode voltar a esta ação ao longo do jogo
	 */
	
	PROCURAR,
	
	/**
	 * Aproximar é a ação resultante da procura de ruido
	 */
	
	APROXIMAR,
	
	/**
	 * Observar é a ação resultante do avistamento de um animal
	 */
	
	OBSERVAR,
	
	/**
	 * Fotografar é a ação regista a fotografia do animal
	 */
	
	FOTOGRAFAR
}
