(cons 2 nil)
(cons 1 (cons 2 nil))
(define x (cons 1 (cons 2 nil)))
(car x)
(cdr x)
(define s (cons (cons 4 (cons 3 nil)) x))
(list? s)
(list 1 2 3 4)
(list 'a 'b)
'(a b c)
'a 
'(1,2)
(define y (cons 1 (cons 2 nil)))
(append y y)
(map even? y)
(map (lambda (x) ( * 2 x)) y)
(filter even? y)
(apply quotient '(10 5))
(apply + '(1 2 3 4))

(define (even-subsets s)
    (if (null? s) nil
        (append (even-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                     (if (even? (car s))
                         (even-subsets (cdr s))
                         (odd-subsets (cdr s))))
                (if (even? (car s)) (list (list (car s)))nil))))
                     
(define (odd-subsets s)
    (if (null? s) nil
        (append (odd-subsets (cdr s))
                (map (lambda (t) (cons (car s) t))
                     (if (odd? (car s))
                         (even-subsets (cdr s))
                         (odd-subsets (cdr s))))
                (if (odd? (car s)) (list (list (car s)))nil))))




