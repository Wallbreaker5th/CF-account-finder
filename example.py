import similarity
import get_submissions
import numpy as np

print(get_submissions.get_ranklist()[:10])

AoLiGei = get_submissions.get_submissions('AoLiGei', 50, 10)
Laurie = get_submissions.get_submissions('Laurie', 50, 10)
tourist = get_submissions.get_submissions('tourist', 50, 10)

print(similarity.similarity(AoLiGei, Laurie),
      similarity.similarity(AoLiGei, tourist),
      similarity.similarity(Laurie, tourist))
print(np.dot(similarity.get_vector(AoLiGei), similarity.get_vector(Laurie)))
