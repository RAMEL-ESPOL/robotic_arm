% Crear una figura nueva
figure;

% Graficar los puntos del workspace
scatter3(X, Y, Z, 3, 'filled', ...
    'MarkerEdgeAlpha', 0.4, ... % Transparencia del borde del marcador
    'MarkerFaceAlpha', 0.4);    % Transparencia de la cara del marcador

% Añadir etiquetas y título
xlabel('Eje X');
ylabel('Eje Y');
zlabel('Eje Z');
title('Workspace del Robot');

% Configuración adicional para mejorar la visualización
grid on;
axis equal;
view(3);

% Supongamos que también tienes el robot en la misma figura
hold on;
show(robot);

% Mejorar la transparencia del robot para que no bloquee los puntos
h = findobj(gca, 'Type', 'Patch');
set(h, 'FaceAlpha', 0.8); % Ajustar la transparencia del robot

% Mantener la gráfica
hold off;