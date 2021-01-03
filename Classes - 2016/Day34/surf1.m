pts = 20;
ACT = repmat(linspace(16, 33, pts), pts, 1);
hsGPA = repmat(linspace(2.4, 4, pts)', 1, pts);
colGPA = 1.2863 + 0.4535*hsGPA + 0.0094*ACT; 

surf(hsGPA, ACT, colGPA)
xlabel('hsGPA')
ylabel('ACT')
zlabel('colGPA [Estimated]')

