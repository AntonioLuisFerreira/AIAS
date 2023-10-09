package jogo.ambiente;
/**
 * Enumeração dos eventos que podem ser usados no ambiente do jogo
 * 
 */
public enum Evento {
	
	/**
	 * Silencio é o evento, o estado inicial
	 * Representa a falta de animais a serem fotografados
	 */
	
	SILENCIO,
	
	/**
	 * Ruido é o evento significativo de um som feito por um animal
	 */
	
	RUIDO,
	
	/**
	 * Animal representa a existencia do aproximamento da personagem em relação ao animal
	 */
	
	ANIMAL,
	
	/**
	 * Fuga é o evento resultante de quando o animal escapou
	 */
	
	FUGA,
	
	/**
	 * Fotografia marca o evento de sucesso na fotografia do animal
	 */
	
	FOTOGRAFIA,
	
	/**
	 * Terminar é o evento que marca o fim do jogo
	 */
	
	TERMINAR
}
