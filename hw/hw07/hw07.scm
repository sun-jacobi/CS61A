(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign num)
  (cond 
    ((> num 0) 1)
    ((= num 0) 0)
    ((< num 0) -1)))

(define (square x) (* x x))

(define (pow x y)
  (if (= y 1)
      x
      (if (even? y)
          (* (square (pow x (/ y 2))))
          (* (square (pow x (/ (- y 1) 2))) x))))

(define (unique s)
  (if (null? s)
      ()
      (cons (car s)
            (unique (filter (lambda (x) (not (eq? x (car s))))
                            (cdr s))))))

(define (replicate x n)
  (define (helper n cache)
    (if (= 0 n)
        cache
        (helper (- n 1) (cons x cache))))
  (helper n nil))

(define (accumulate combiner start n term)
  (define (helper t n cache)
    (if (= n 0)
        cache
        (helper (+ t 1) (- n 1) (combiner cache (term t)))))
  (helper 1 n start))

(define (accumulate-tail combiner start n term)
  (define (helper t n cache)
    (if (= n 0)
        cache
        (helper (+ t 1) (- n 1) (combiner cache (term t)))))
  (helper 1 n start))

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 (list 'map
       (list 'lambda (list var) map-expr)
       (list 'filter
             (list 'lambda (list var) filter-expr)
             lst)))
