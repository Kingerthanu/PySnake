# PySnake
A Pygame I made in which you use the arrow keys to move around and play a game of snake.

Was one of my first projects and helped me understand how inputs are handled as well as how to display on the screen to a user. It also taught me more about efficient coding practices and how to traverse through index to allow for batch checks on things like the snakes body as well as on berrys if more are implemented.

----------------------------------------------------------------------------

<img src="https://github.com/Kingerthanu/PySnake/assets/76754592/2f13e060-4fe9-41df-b3ff-579ef4819953" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/2f13e060-4fe9-41df-b3ff-579ef4819953" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/2f13e060-4fe9-41df-b3ff-579ef4819953" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/2f13e060-4fe9-41df-b3ff-579ef4819953" alt="Cornstarch <3" width="55" height="49">


**The Breakdown:**

  This Program Works On Python And Its Pre-Packaged Pygame Window Generator.

  Using The Library, We Declare A Snake Class Definition In Which Works To Have Associated Squares Which Represent The Snakes Body On The Screen. This Includes Our Draw Calls And Movement Functionality. We Also Have A Berry Class In Which Works To Only Have A Render Function.

  In Our Main/Driver Function We Set Up A New Movement Event Every 50ms In Which Will Check Globals Like Our Selected Direction Of Motion To Draw/Move Our Snake. In Our Current Build Of This, We Only Have 1 Berry Spawned At A Time And When One Is Collected By The User, Another Is Randomly Spawned On The Map Plane.

  Unlike Some Other Grid-Based Programs That I've Made, This One Is More Dynamic As Instead Of Checking If A "Cell" Is Filled Via A 2D Array Struct, We Instead Check By Its Direct xy-Coordinate. This Can Add Jank If Misaligned, But Works Well In Our Closed System.

<img src="https://github.com/Kingerthanu/PySnake/assets/76754592/91450e81-0355-4a5a-9d6c-1077a7b7d07d" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/91450e81-0355-4a5a-9d6c-1077a7b7d07d" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/91450e81-0355-4a5a-9d6c-1077a7b7d07d" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/91450e81-0355-4a5a-9d6c-1077a7b7d07d" alt="Cornstarch <3" width="55" height="49">

----------------------------------------------------------------------------

<img src="https://github.com/Kingerthanu/PySnake/assets/76754592/861a459c-8d5f-4296-9e9c-14f96b1e5f19" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/861a459c-8d5f-4296-9e9c-14f96b1e5f19" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/861a459c-8d5f-4296-9e9c-14f96b1e5f19" alt="Cornstarch <3" width="55" height="49"><img src="https://github.com/Kingerthanu/PySnake/assets/76754592/861a459c-8d5f-4296-9e9c-14f96b1e5f19" alt="Cornstarch <3" width="55" height="49">

**Features:**

<img src="https://github.com/Kingerthanu/PySnake/assets/76754592/f040e085-a252-4ebd-81f6-d5c66cd23b52" alt="Cornstarch <3" width="115" height="99">

  ![2024-01-0923-28-41-ezgif com-optimize](https://github.com/Kingerthanu/PySnake/assets/76754592/108b8324-1ecb-416f-bf6a-201a2b210cc2)
![snake2](https://github.com/Kingerthanu/PySnake/assets/76754592/402688ec-eace-4372-a55e-71d72e02be00)
![snake1](https://github.com/Kingerthanu/PySnake/assets/76754592/9f30502f-ba1e-4f36-98aa-ecba9501bab3)
![snake3](https://github.com/Kingerthanu/PySnake/assets/76754592/23bdbfe7-44b1-4886-94f2-0bb8943f5a72)




<img src="https://github.com/Kingerthanu/PySnake/assets/76754592/eff9e463-4a96-4857-aae3-2777329a30c1" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/eff9e463-4a96-4857-aae3-2777329a30c1" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/eff9e463-4a96-4857-aae3-2777329a30c1" alt="Cornstarch <3" width="55" height="49"> <img src="https://github.com/Kingerthanu/PySnake/assets/76754592/eff9e463-4a96-4857-aae3-2777329a30c1" alt="Cornstarch <3" width="55" height="49">
