package jogo.ambiente;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Esta classe vai permitir simular e tratar a sequência de 
 * eventos do ambiente em que o jogo decorre
 * 
 * @author amvlf
 *
 */

public class Ambiente {
	
	/**
	 * 3 atributos privados
	 * 
	 * O primeiro atributo, evento permite traduzir o evento mais recente
	 * 
	 * O segundo atributo sc será o input introduzido pelo o utilizador para influenciar o jogo
	 * 
	 * O terceiro, é um map onde vão estar os eventos com as suas respetivas keywords
	 */
	private Evento evento;
	private Scanner sc = new Scanner(System.in);
	private Map<String, Evento> eventos;
		
	/**
	 * O construtor inicializa o map com os eventos e as suas respetivas keywords
	 */
	public Ambiente() {
		eventos = new HashMap<>();
        eventos.put("s", Evento.SILENCIO);
        eventos.put("r", Evento.RUIDO);
        eventos.put("a", Evento.ANIMAL);
        eventos.put("f", Evento.FUGA);
        eventos.put("o", Evento.FOTOGRAFIA);
        eventos.put("t", Evento.TERMINAR);
	}
	
	/**
	 * Método que retorna o evento atual a ser utilizado
	 * 
	 *@return Evento atual
	 */
	
	public Evento getEvento() {
		return evento;
	}
	
	/**
	 * O Método evoluir consiste em passar para o próximo evento,
	 * dar print do mesmo
	 */
	public void evoluir() {
		evento = gerarEvento();
		mostrar();
	}
		
	/**
	 * Método responsável por gerar o próximo evento,
	 * perguntando ao utilizador qual evento pertende executar
	 * 
	 * @return novo Evento
	 */
	private Evento gerarEvento() {
		System.out.println("Qual o próximo Evento?");
		String tecla = sc.next();
		return eventos.get(tecla);
	}
	
	/**
	 * Faz print na consola do evento a ser utilizado
	 */
	
	private void mostrar() {
		if(evento != null) {
			System.out.println("Evento: " + evento.toString());
		}
	}
	
}
