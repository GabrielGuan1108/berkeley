(define (accumulate combiner start n term)
  (define (helper index)
          (cond
            ((<= index (- n 1)) (combiner (term index) (helper (+ 1 index))))
            ((= index n) (term n))
          )
  )
  (combiner start (helper 1))
)

(define (accumulate-tail combiner start n term)
(define (helper index)
        (cond
          ((<= index (- n 1)) (combiner (term index) (helper (+ 1 index))))
          ((= index n) (term n))
        )
)
(combiner start (helper 1))
)

(define (rle s)
(if (null? s)
    s
    (begin
(define (helper first second times)
          (cond
          ((null? second) (cons-stream (list first times) nil))
          ((= first (car second)) (helper first (cdr-stream second) (+ times 1)))
          (else (cons-stream (list first times) (helper (car second) (cdr-stream second) 1)))
          )
)
(helper (car s) (cdr-stream s) 1)
))
)
