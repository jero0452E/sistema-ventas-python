# Tienes dos listas de clientes
email_newsletter = ["ana@gmail.com", "luis@hotmail.com", "maria@gmail.com", "pedro@outlook.com", "ana@gmail.com", "luis@hotmail.com"]
compraron = ["ana@gmail.com", "pedro@outlook.com", "carlos@gmail.com"]

email_newsletter_set = set(email_newsletter)
compraron_set = set(compraron)
print(len(email_newsletter_set))
# 1) ¿Cuántos correos ÚNICOS hay en la lista del newsletter?
#    (pista: set + len)

# 2) ¿Qué correos aparecen en el newsletter pero NUNCA han comprado?
#    (pista: resta de sets)
print(email_newsletter_set-compraron_set)

# 3) ¿Qué clientes compraron pero NO están en el newsletter?
#    (pista: resta en sentido contrario)
print(compraron_set-email_newsletter_set)
# 4) ¿Cuántos correos únicos hay en total entre ambas listas?
#    (pista: unión + len)
print(len(email_newsletter_set.union(compraron_set))) # .union se puede remplazar por el operador | (pipe)