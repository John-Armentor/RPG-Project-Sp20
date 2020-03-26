Within our team our development process is as follows:

--BackLog--
New features/fixes/Reworkings (Stories) are outlined in our Project backlog within this repository.  

--In Progress--
When a Backlog task is selected, it is then made into an issue report and assigned to a developer on the team and moved into the In Progress section of the project board.  The developer works on the issue in their personal workspace.

--Peer Review--
Once the developer feels confident in the functionality and the implementation, they will merge it into their personal testspace.  The story is now moved from In Progress into Peer Review on the project board.  Upon reaching the testspace, thorough code review and runtime testing occurs to ensure the quality of the code by other developers who are assigned to review the story. 

After local, individual testing was completed and one reviewer approves the code, a Pull Request is created to move from that individual testspace into our joint testspace.  At this point, two developers review the joint testspace to ensure that all combined projects are working together without any conflict.

--Dev Complete--
When we as a team reach a solid development point within our joint testing branch and no conflicts were found, a Pull Request will be made from Joint Testing into our main branch.  At this point, the story will be moved from Peer Review into Dev Complete on the project board.

--In Main--
Once the joint testing branch has been moved into the master branch, the story is moved from Dev Complete into In Main on the project board.  At this point, each developer is responsible for making sure that their local workspace is kept up-to-date with the master branch.
