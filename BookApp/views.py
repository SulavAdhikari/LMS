from rest_framework import generics, permissions, views, status
from rest_framework.response import Response


from .models import Book, BookDetail, BorrowedBook
from .serializers import BookSerializer, BookDetailSerializer, BorrowedBookCreateSerializer, BorrowedBookSerializer
from UserApp.authentication import CustomJWTAuthentication
from datetime import datetime


class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [CustomJWTAuthentication]



class ListAllBooksView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class GetBookByIdView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'



class AssignUpdateBookDetailsView(views.APIView):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [CustomJWTAuthentication]
    lookup_field = 'id'
    
    def get(self, request, id):
        try:
            book_detail = BookDetail.objects.get(book=id)
            serializer = BookDetailSerializer(book_detail)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BookDetail.DoesNotExist:
            return Response({'error': 'BookDetail not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id):
        serializer = BookDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data, id=id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            book_detail = BookDetail.objects.get(book=id)
        except BookDetail.DoesNotExist:
            return Response({'error': 'BookDetail not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookDetailSerializer(book_detail, data=request.data)
        if serializer.is_valid():
            serializer.update(validated_data=serializer.validated_data, id=id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class BorrowBookView(generics.CreateAPIView):
    
    serializer_class = BorrowedBookCreateSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class ReturnBookView(generics.UpdateAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookCreateSerializer
    lookup_field = 'id'
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListAllBorrowedBooksView(generics.ListAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BorrowedBook.objects.filter(user=user)