(ns final.core)

;;---------------------------
;; Mayank Jariwala - 40075419
;;---------------------------

;;---------------------------------------------------------------------------------------
;;                               Variable Declaration Starts
;;---------------------------------------------------------------------------------------

(def customers (atom()))
(def products (atom()))
(def sales (atom ())) 

(def productref (atom()))
(def custref (atom ()))
(def salesref (atom ()))

;;---------------------------------------------------------------------------------------
;;                                Variable Declaration Ends
;;---------------------------------------------------------------------------------------


;;---------------------------------------------------------------------------------------
;;                               Functions Definition Starts
;;---------------------------------------------------------------------------------------

(defn _split [y]
  (clojure.string/split y #"\|"))

(defn apply_quotes [x]
  (mapv #(str "\""(clojure.string/trim-newline %)"\"" ) x))


;;Just to check whether key value exists in hashmap
(defn checkForKeyValue [k v]
  (fn [m]
    (= v (m k))))


;;--------------------------- Sorting Function By Specific Key ------------------------ 
(defn sort-sales-data
  [el1 el2]
  (if (or  (> (:salesid el1) (:salesid el2))
    (and (= (:salesid el1) (:salesid el2))(> (:salesid el1) (:salesid el2))))
    true
    false)
)

(defn printData [filename , module]
   (def x (clojure.string/split (slurp filename) #"\n"))
   (def _vec (map (fn[y] (_split y)) x))
   (def _fmap (sort-by :id (map #(hash-map :id (Integer/parseInt (first %1)) :val (vec (rest %1))) _vec)))
   ;;If Module is Customer
(if (= "cust" module)
     (do
       (doseq [_item _vec]
          (swap! custref conj (hash-map :custid (nth _item 0) :name (nth _item 1) :street (nth _item 2) :cell (nth _item 3))))
         (doseq [_item _fmap]
          (swap! customers conj _item))
      )
   )
  
   ;;If Modue is Sales
  (if (= "sales" module)
     (do
       (doseq [_item _vec]
          (swap! salesref conj (hash-map :salesid (Integer/parseInt (nth _item 0)) :custid (nth _item 1) :prodid (nth _item 2) :quantity (nth _item 3))))
       (doseq [_item _fmap]
         (swap! sales conj _item)))
  )
 
   ;;If Module is Products
  (if (= "products" module)
     (do
       (doseq [_item _vec]
          (swap! productref conj (hash-map :prodid (nth _item 0) :name (nth _item 1) :price (nth _item 2))))
       (doseq [_item _fmap]
         (swap! products conj _item)))
   )
)

;;--------------------------- Show Sales Table Function ----------------------------
(defn formattedData [_i]
   (println (clojure.string/replace 
       (format "%s:[\"%s\"\t\"%s\"\t\"%s\"]" 
               (get _i :salesid) (get _i :custid) (get _i :prodid) (get _i :quantity)) #"\r" ""))
)

(defn returnCustomerNameById []
  (def x (atom ()))
  (doseq [_item (sort (comp sort-sales-data) @salesref)]
     (doseq [_custitem @custref]
        (if (= (get _custitem :custid) (get _item :custid))
          (do
           (def cust_name (get _custitem :name))
            (assoc _item :custid cust_name)
         )
        )
     )
     (doseq [_proditem @productref]
        (if (= (get _proditem :prodid) (get _item :prodid))
          (do
           (def prod_name (get _proditem :name))
         )
        )
     )
    (swap! x conj (assoc (assoc _item :custid cust_name) :prodid prod_name))
   )
   (doseq [_i @x]
       (formattedData _i)
   )
)

;;--------------------------- Calculate User Cost Function ----------------------------
(defn calculateCost [name]
  (def x (atom ()))
  (def sumup (atom ()))
  (doseq [_item @salesref]
     (doseq [_custitem @custref]
        (if (= (get _custitem :custid) (get _item :custid))
          (do
           (def cust_name (get _custitem :name))
            (assoc _item :custid cust_name)
         )
        )
     )
     (doseq [_proditem @productref]
        (if (= (get _proditem :prodid) (get _item :prodid))
          (do
           (def prod_name (get _proditem :name))
           (def prod_price (get _proditem :price))
         )
        )
     )
    (swap! x conj (assoc (assoc _item :custid cust_name) :prodid prod_name :price prod_price) )
   )
  (def bool_check (empty? (filter (checkForKeyValue :name name) @custref)))
  (if (= bool_check false)
  (do  
  (doseq [_i @x]
     (if (= (get _i :custid)  name)
      (do
         (def tmp_price (Float/parseFloat (get _i :price)))
         (def tmp_quantity (Float/parseFloat (get _i :quantity)))
         (def x_temp  (Float/parseFloat (format "%.2f" (* tmp_price tmp_quantity))))
         (swap! sumup conj x_temp)
      )
    )
   )
   (if (empty? @sumup)
      (println (clojure.string/capitalize name)":"(str "$0") )

      (println (clojure.string/capitalize name)":"(str "$" (format "%.2f" (reduce + @sumup))))
   )
   )
    (println "No Customer With Such Name Exists [** NOTE: Names are case Sensitive **]")
   )
)


;;--------------------------- Calculate Product Sale Function ----------------------------
(defn calculateProductSale [name]
  (def x (atom ()))
  (def sumup (atom ()))
  (doseq [_item @salesref]
     (doseq [_custitem @custref]
        (if (= (get _custitem :custid) (get _item :custid))
          (do
           (def cust_name (get _custitem :name))
            (assoc _item :custid cust_name)
         )
        )
     )
     (doseq [_proditem @productref]
        (if (= (get _proditem :prodid) (get _item :prodid))
          (do
           (def prod_name (get _proditem :name))
           (def prod_price (get _proditem :price))
         )
        )
     )
    (swap! x conj (assoc (assoc _item :custid cust_name) :prodid prod_name :price prod_price) )
   )
   (def bool_check (empty? (filter (checkForKeyValue :name name) @productref)))
   (if  (= bool_check false)
   (do
   (doseq [_i @x]
     (if (= (get _i :prodid) name)
      (do
        (def x (Integer/parseInt (clojure.string/trim (get _i :quantity))))
        (swap! sumup conj x)
      )
    )
   )
   (if (empty? @sumup)
    (println (clojure.string/capitalize name)": 0")

    (println (clojure.string/capitalize name)":" (reduce + @sumup))
   )
   )
   (println "No Such Product Found [** NOTES: Names are Case Sensitive **]")
   )

)

;;--------------------------- Display Menu Function ------------------------------------
(defn showMenu []
(println "\n***** Sales Menu ******")
(println "------------------------")
(println "1. Display Customer Table")
(println "2. Display Product Table")
(println "3. Display Sales Table")
(println "4. Total Sales for Customer")
(println "5. Total Count For Product")
(println "6. Exit")
(println "Enter Choice From Above Menu")

 ;;Variable To Get Menu Options From User
(def choice (read-line))

 ;;Switch Case To Invoke Functions
(case choice 
     "1" (
          (def cust_list (sort-by :id (deref customers)))
          (doseq [_item cust_list]
              (println (get _item :id)":"(apply_quotes (get _item :val))))
          (showMenu)
       ) 
     "2" (
          (def prod_list (sort-by :id (deref products)))
          (doseq [_item prod_list]
             (println (get _item :id)":"(apply_quotes (get _item :val))))
          (showMenu)
       )
     "3" (
           (returnCustomerNameById)
           (showMenu)
       )
     "4" (
           (println "Enter Customer Name")
           (def user_name (read-line))
           (calculateCost user_name)
           (showMenu)
       )
     "5" (
           (println "Enter Product Name")
           (def product_name (read-line))
           (calculateProductSale product_name)
           (showMenu)
       )
     "6" (
           (println "Good Bye")
           (System/exit 0)
         )
     ((println "Oops!! Please Select Option From Above Menu")
     (showMenu))
)
)

;;---------------------------------------------------------------------------------------
;;                               Functions Definition End
;;---------------------------------------------------------------------------------------

;;---------------------------------------------------------------------------------------
;;                               Functions Call Start
;;---------------------------------------------------------------------------------------

(printData "cust.txt" "cust")
(printData "sales.txt" "sales")
(printData "prod.txt" "products")
(showMenu)

;;---------------------------------------------------------------------------------------
;;                               Functions Call End
;;---------------------------------------------------------------------------------------