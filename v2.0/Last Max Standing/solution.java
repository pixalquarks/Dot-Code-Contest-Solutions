static int LastMaxStanding(int numberOfElement, List<Integer> numbers){
        //to store maximum element of the current list.
        int x=0;

        //run the loop till we are left with single element in the list.
        while (numbers.size()>1){
            x = Collections.max(numbers);  
            int ind=numbers.indexOf(x);  // to find the index of current maximum element.

            /* check if next two elements are in increasing order then
              delete maximum and adjacent to maximum element otherwise remove the maximum element only. */
            if(numbers.get((ind+1)%numbers.size())<numbers.get((ind+2)%numbers.size())){
                numbers.remove(ind%numbers.size());
                numbers.remove(ind%numbers.size());
            }
            else
                numbers.remove(ind%numbers.size());

        }

        /* if single element is left, then that's our required answer otherwise return the value stored in 'x',the
         one on which last operation has been performed. */
        if(numbers.size()==1)
            x=numbers.get(0);
        return x;
    }