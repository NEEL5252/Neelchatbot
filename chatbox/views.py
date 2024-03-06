from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *

# Create your views here.
@csrf_exempt
def add_order(request):
    # print(request.body)

    if request.method == 'POST':
        data = json.loads(request.body)
        responseId = data.get('responseId')
        # print(data)
        intent = data.get('queryResult').get('intent')['displayName']

        if intent == 'new-order':
            get, create = new_user.objects.get_or_create(responseId = responseId)
            response = {
                "fulfillmentText" : "Ready to take new order!"
            }
            global user
            user = get
            return JsonResponse(response)
        # Saving order for the user
        elif intent == 'add-order:context:new-order':   
            item = data.get('queryResult').get('parameters')['total-items']
            quantity = data.get('queryResult').get('parameters')['number']
            for i in range(len(item)):
                new_order.objects.create(
                    user = user,
                    item_name = item[i],
                    quantity = quantity[i]
                )
            response = {
                "fulfillmentText" : f"Your order has been recorded! with order Id {user.id}"
            }
            return JsonResponse(response)

        elif intent == 'tracking-order:context:track-order':
            queryText = data.get('queryResult').get('queryText')

            if int(queryText) == int(user.id):
                order_details = new_order.objects.filter(user = user).values()
                orders = []
                for i in order_details:
                    data = {
                        i['quantity'] : i['item_name'],
                    }
                    orders.append(list(data.items()))
                # print(order_details)
                response = {
                    "fulfillmentText" : f"Your order has been dispatched with! with order Id {user.id} and order {orders}"
                }
                return JsonResponse(response)
            else:
                response = {
                    "fulfillmentText" : f"No order found for order Id {queryText}! Please check your order Id and try again!"
                }
                return JsonResponse(response)

        
        elif intent == "remove_order:context:new_order":
                # user_id = user.id
                # item = data.get('queryResult').get('parameters')['total-items']

                quantity = data.get('queryResult').get('parameters')['number']

                ordertodelete = new_order.objects.get(user = user, quantity = quantity[0])
                print(ordertodelete)
                if not ordertodelete:
                    response = {
                        "fulfillmentText" : f"No any order has been found order Id {user.id}!!! Restart Again"
                    }
                    return JsonResponse(response)

                ordertodelete.delete()
                order_details = new_order.objects.filter(user = user).values()
                orders = []
                for i in order_details:
                    data = {
                        i['quantity'] : i['item_name'],
                    }
                    orders.append(list(data.items()))
                response = {
                    "fulfillmentText" : f"Your item has been removed for order Id {user.id} remain items are {orders}"
                }
                return JsonResponse(response)

    return JsonResponse({"message" : "Something error occured"})

def index(request):
    return render(request, "index.html")