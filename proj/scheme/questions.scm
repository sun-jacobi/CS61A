(define (caar x) (car (car x)))

(define (cadr x) (car (cdr x)))

(define (cdar x) (cdr (car x)))

(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (cons-all first rests) 'replace-this-line)

(define (zip pairs) 'replace-this-line)

; ; Problem 16
; ; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (tail s n)
    (if (eq? s nil)
        ()
        (cons (cons n (cons (car s) nil))
              (tail (cdr s) (+ n 1)))))
  (tail s 0))

; END PROBLEM 16
; ; Problem 17
; ; List all ways to make change for TOTAL with DENOMS
(define (cons-all first rests)
  (if (eq? rests nil)
      nil
      (cons (cons first (car rests))
            (cons-all first (cdr rests)))))

(define (list-change total denoms)
  ; BEGIN PROBLEM 17    
  (if (or (= total 0) (eq? denoms nil))
      ()
      (cond 
        ((< total (car denoms))
         (list-change total (cdr denoms)))
        ((= total (car denoms))
         (cons (cons (car denoms) nil)
                 (list-change total (cdr denoms))))
        (else
         (append (cons-all (car denoms)
                           (list-change (- total (car denoms)) denoms))
                 (list-change total (cdr denoms)))))))

; END PROBLEM 17
; ; Problem 18
; ; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))

(define define? (check-special 'define))

(define quoted? (check-special 'quote))

(define let? (check-special 'let))

; ; Converts all let special forms in EXPR into equivalent forms using lambda
(define (zip expr)
  (define (first expr)
    (if (eq? expr nil)
        ()
        (cons (car (car expr)) (first (cdr expr)))))
  (define (second expr)
    (if (eq? expr nil)
        ()
        (cons (car (cdr (car expr))) (second (cdr expr)))))
  (list (first expr) (second expr)))

(define (let-to-lambda expr)
  (cond 
    ((atom? expr)
     ; BEGIN PROBLEM 18
     expr
     ; END PROBLEM 18
    )
    ((quoted? expr)
     ; BEGIN PROBLEM 18
     expr
     ; END PROBLEM 18
    )
    ((or (lambda? expr) (define? expr))
     (let ((form (car expr))
           (params (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 18
       (if (eq? (cdr body) nil)
           (list form params (car body))
           (list form
                 params
                 (car body)
                 (let-to-lambda (cadr body))))
       ; END PROBLEM 18
     ))
    ((let? expr)
     (let ((values (cadr expr))
           (body (cddr expr)))
       ; BEGIN PROBLEM 18
       (cons (list 'lambda
                   (car (zip values))
                   (let-to-lambda (car body)))
             (map let-to-lambda (car (cdr (zip values)))))
       ; END PROBLEM 18
     ))
    (else
     ; BEGIN PROBLEM 18
     (if (eq? expr nil)
         ()
         (cons (let-to-lambda (car expr))
               (let-to-lambda (cdr expr))))
     ; END PROBLEM 18
    )))
