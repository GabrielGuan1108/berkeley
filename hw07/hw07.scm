(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    ((> x 0) 1))
)

(define (square x) (* x x))

(define (pow b n)
  (cond
  ((= n 1) b)
  ((even? n) (square (pow b (/ n 2))))
  ((odd? n) (* b (pow b (- n 1)))))
)

(define (ordered? s)
  (cond
    ((null? s) #t)
    ((null? (cdr s)) #t)
    ((<= (car s) (cadr s)) (ordered? (cdr s)))
    (else #f))
)
