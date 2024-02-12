(defun sum (term a next b)
  (defun iter (a result)
    (if (> a b)
        result
        (iter (next a) (+ result (term a)))))
  (iter a 0))
