 ## Ethical Hacking Problem Solver microservice 



This django based solution that when consulted gets the user the shortest number containing every sequence in a provided list.


## api_solve_list method
-Input:{iteraciones : number of iterations desired in order to solve the problem. The bigger this number is more certaity of having the smallest number there is for the list sequence .
       new_list : other list in case of wanting to run the problem with a diferent list diferent from the keylog.txt
}

-Output:{numero : shortest number that solves the problem 
}

- Get the solution to the problem with the original keylog.txt list
- Get the soution of the problem with a list passed in the json file of the get request.
 
