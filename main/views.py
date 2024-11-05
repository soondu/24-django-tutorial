# Create your views here.
from decimal import Decimal

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.serializers import (
    CalculatorSerializer,
    CalculatorResponseSerializer,
)


class CalculatorAPIView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CalculatorSerializer

    def post(self, request):
        # de-serialization
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result: Decimal = None
        ## assignment1: 이곳에 과제를 작성해주세요
        input_a=serializer.validated_data['input_a']
        input_b=serializer.validated_data['input_b']
        operator=serializer.validated_data['operator']

        try:
            num1=Decimal(input_a)
            num2=Decimal(input_b)
        except InvalidOperation:
            return Response({"error": "Invalid number"})

        if operator == '+':
            result = num1+num2
        elif operator == '-':
            result = num1-num2
        elif operator == '*':
            result = num1*num2
        elif operator == '/':
            if num2==0:
                return Response({"error": "Cannot divide by zero"})
            result = num1/num2
        else:
            return Response({"error": "Invalid operator"})

        ## end assignment1

        # serialization
        return Response(CalculatorResponseSerializer({"result": result}).data)
