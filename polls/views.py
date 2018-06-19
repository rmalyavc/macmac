from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from cart.forms import CartAddProductForm

from .models import Choice, Question, Product, Category, Brands

# def ProductDetail(request, id):
#     product = get_object_or_404(Product, id=id)
#     cart_product_form = CartAddProductForm()
#     return render_to_response('polls/product.html',
#                              {'product': product,
#                               'cart_product_form': cart_product_form})


class RegisterView(generic.ListView):
    template_name = 'polls/index3.html'
    
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
    # def check():
    #     if not form["username"]:
    #         return 1;

class CatalogueView(generic.ListView):
    template_name = 'polls/index2.html'
    context_object_name = 'latest_product_list'
    
    def get_queryset(self):
        # if request.method == 'GET':
        #     category = request.GET.get('category', '')
        # cart_product_form = CartAddProductForm()
        return Product.objects.all()
        # return cart_product_form
        
    # def filtred(self, request):
    #     category = request.GET.get('category', None)
    #     return Product.objects.all().filter(category=category)
    
class CategoryView(generic.ListView):
    template_name = 'polls/index2.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.all()
        
class BrandsView(generic.ListView):
    template_name = 'polls/index2.html'
    context_object_name = 'brands'
    
    def get_queryset(self):
        return Brands.objects.all()
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

