import pytest
 
from bibliotheque.catalogue import Bibliotheque
from bibliotheque.livre import Livre
 
 
@pytest.fixture
def livre():
    return Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus")
 
 
@pytest.fixture
def biblio():
    # Préparation (setup) : exécutée avant le test
    b = Bibliotheque()
    b.ajouter(Livre("978-2-07-040850-4", "Le Petit Prince", "Antoine de Saint-Exupéry"))
    b.ajouter(Livre("978-2-07-036002-4", "L'Étranger", "Albert Camus"))
    b.ajouter(Livre("978-2-07-036822-8", "La Peste", "Albert Camus"))
    yield b  # le test s'exécute ici, avec b
    # Nettoyage (teardown) : exécuté après le test, même s'il a échoué
    isbns = [livre.isbn for livre in b.livres]
    assert len(isbns) == len(set(isbns)), "ISBN en double dans le catalogue"
