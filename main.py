import process

 if __name__ == '__main__':
     #
     data = gather.get_data()
     if 'error' in data:
         print(data['error'])
