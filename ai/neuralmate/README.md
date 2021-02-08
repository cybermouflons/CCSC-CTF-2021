# Neuralmate
**Category:** artificial intelligence

**Author:** \_Roko'sBasilisk\_

## Description
Benny is showing off again... intelligence is a trait of his, but so is laziness. This time he came up with a neural network for recognizing the position of chess pieces on the board for him without even looking.

He gave you 3 boards and challenged you to beat him in a single move. He sounds confident... but maybe you can mess with his brain.

Beat him in all three boards to get the flag.

## Points
500

## Solution

<details>
 <summary>Reveal Spoiler</summary>

The main objective of this challenge is to beat Benny with a single move in all of the 3 chess boards that he provided. Interestingly you can send the state of the board back as an image but the service checks that the sent image is almost visually similar to the original one. 

That being said, normally it is not possible to check mate in one move, but it is possible to use an adverarial attack on the neural netowkr model so that it is fooled and reads a board in which is possible to check mate in one move while the similarity threshold is not exceeded.

The steps for solving this challenge are as follows:
1. Identify a similar board with the original one from which Benny can be check mated in a single move.
2. Using an adversarial attack create an adversarial example of the target boards while satisfying the similarity requirements
3. Send that to Neuralmate service and execue the check mate move.
4. Repeat the above 3 times.

A solution the performs the above steps is provided in [solve.py](./solution/solve.py)

</details>