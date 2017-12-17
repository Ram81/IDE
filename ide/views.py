import sys
import yaml
import copy

from utils.shapes import get_shapes
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def calculate_parameter(request):
    if request.method == 'POST':
        net = yaml.safe_load(request.POST.get('net'))
        try:
            netObj = copy.deepcopy(net)
            for layerId in netObj:
                for param in netObj[layerId]['params']:
                    netObj[layerId]['params'][param] = netObj[layerId]['params'][param][0]
            # use get_shapes method to obtain shapes of each layer
            netObj = get_shapes(netObj)
            for layerId in net:
                net[layerId]['shape'] = {}
                net[layerId]['shape']['input'] = netObj[layerId]['shape']['input']
                net[layerId]['shape']['output'] = netObj[layerId]['shape']['output']
        except BaseException:
            return JsonResponse({
                'result': 'error', 'error': str(sys.exc_info()[1])})
        return JsonResponse({'result': 'success', 'net': net})
