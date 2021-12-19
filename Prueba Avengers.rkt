#lang racket

(define-struct participante (nombre puntaje dinero))


(println "¿Eres un verdadero fan de las peliculas Marvel?")
(println "Ingresa tu informacion y responde las siguientes preguntas")

;;input: string -> string
;;Escribe un mensaje en la consola
;;Y recibe un elemento con read
(define (input mensaje)
  (begin (display mensaje)
         (newline)
         (read)
         )
  )

(define jugador1 (make-participante (input "Ingrese su primer nombre") 0 0))

;(define (ACTIVAR)
;  (begin
;    (crearJugador (input "Ingrese su nombre: "))
;  )
;  )



;(participante-nombre jugador1)
;(participante-puntaje jugador1)
;(participante-dinero jugador1)


(define pregunta1
  (begin
    (println "¿En qué año se estrenó la primera película de Iron Man, que lanzó el Marvel Cinematic Universe?")
    (println "A) 2005")
    (println "B) 2008")
    (println "C) 2010")
    (println "C) 2012")
    (let ([opcion (input "Ingrese su respuesta: ")])
  (cond
    [(equal? opcion 'B)
      (begin (make-participa) )]
    [(equal? opcion "P")
      (begin
        (hallarP (input "Ingrese A")
                 (input "Ingrese i")
                 (input "Ingrese n"))
        )]

    
    [(number? opcion) (print "Lo siento, No se permiten numeros")]
    [else (print "Lo siento, escriba entre comillas 'A' o 'P'")])
  )))