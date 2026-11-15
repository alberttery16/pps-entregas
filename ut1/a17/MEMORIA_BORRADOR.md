# ACT_UT1_4 · Solidity + Git

**Borrador de memoria. No entregar sin completar las evidencias.**

Autor: Albert Grigore (confirmar nombre completo de portada).
NIA: pendiente.
Módulo: Puesta en Producción Segura.
Fecha de preparación: 15 de noviembre de 2026.

## Índice

1. Introducción
2. Lectura de los tres artículos
3. CryptoZombies: las seis lecciones
4. Learn Git Branching: Main
5. Learn Git Branching: Remote
6. Análisis del contrato de la lección 1
7. Desbordamiento y SafeMath
8. SafeMath32, SafeMath16 y Solidity 0.8
9. Conclusión
10. Bibliografía

## Introducción

Esta actividad compara la ejecución de contratos inteligentes con la de programas locales y estudia un riesgo concreto: el desbordamiento de enteros. También relaciona las operaciones de Git con la organización del repositorio de entregas. Se utiliza el contenido oficial de CryptoZombies y la documentación de Solidity y Ethereum como apoyo.

**Estado del documento:** borrador técnico. No acredita haber completado las seis lecciones ni los 25 niveles del simulador. Faltan las capturas de logro, los tres artículos concretos del aula y los datos de portada. Las explicaciones siguientes están preparadas para contrastarlas con las prácticas realizadas.

## Parte 1 · Lectura de los tres artículos

La EVM es la máquina virtual que ejecuta el bytecode de los contratos de Ethereum.
Se parece a CPython en que ejecuta instrucciones intermedias y no directamente el código fuente escrito por el programador.
CPython normalmente ejecuta un programa en un proceso local; la EVM permite reproducir la transición de estado de una blockchain.
Los clientes de ejecución de los nodos que verifican los bloques ejecutan las transacciones y comprueban el resultado de los contratos.
El código debe producir resultados deterministas: no puede leer libremente un archivo local o consultar una web como haría un programa Python.
El gas mide el trabajo computacional y limita cuánto puede ejecutar una transacción.
Su coste se paga mediante comisiones en ETH; gas es una unidad de trabajo, no el nombre de la moneda.
Si se agota durante la ejecución, se revierten los cambios de esa ejecución, aunque el trabajo consumido sigue teniendo coste.

Ejemplo: crear un zombi añade datos al almacenamiento persistente del contrato y consume gas. Un programa Python que añade un objeto a una lista local no necesita consenso entre nodos ni paga una comisión de Ethereum. Una consulta local con `eth_call` puede simular la ejecución sin enviar una transacción con comisión, aunque también está sujeta a límites del nodo.

Fuentes de apoyo: [EVM](https://ethereum.org/developers/docs/evm/) y [gas](https://ethereum.org/developers/docs/gas/). Falta contrastar el texto con los artículos del aula «Blockchain Basics Ethereum Explained», «How Ethereum Works» y «Ethereum Virtual Machine».

## Parte 2 · CryptoZombies: las seis lecciones

Curso: [Solidity: Beginner to Intermediate Smart Contracts](https://cryptozombies.io/solidity). Usar la cuenta corporativa indicada por el profesor y el mismo navegador. Las siguientes descripciones explican el contenido del curso; los logros permanecen pendientes de comprobar.

### Lección 1 · Making the Zombie Factory

Se construye una fábrica que recibe un nombre, calcula un ADN y guarda un zombi. Se introducen contratos, variables de estado, tipos enteros, estructuras, arrays, funciones y eventos.

**Captura pendiente:** `capturas/cryptozombies-01.png`.
Pie previsto: «Figura 1. Lección 1 completada: fábrica de zombis y elementos básicos de Solidity».

### Lección 2 · Zombies Attack Their Victims

Se relacionan zombis y propietarios mediante mappings y `msg.sender`. Se incorpora alimentación y multiplicación, utilizando herencia, interfaces y referencias `storage` frente a copias `memory`.

**Captura pendiente:** `capturas/cryptozombies-02.png`.
Pie previsto: «Figura 2. Lección 2 completada: propietarios, alimentación e interacción entre contratos».

### Lección 3 · Advanced Solidity Concepts

Se añaden restricciones de acceso, niveles y tiempos de espera. Se estudian modificadores, propiedad del contrato, costes de gas y el uso de tipos de menor tamaño para organizar los datos.

**Captura pendiente:** `capturas/cryptozombies-03.png`.
Pie previsto: «Figura 3. Lección 3 completada: control de acceso y conceptos avanzados de Solidity».

### Lección 4 · Zombie Battle System

Se desarrolla el combate y se actualizan victorias, derrotas y niveles. Se practican funciones `payable`, pagos y cálculos para decidir el resultado de una batalla; la aleatoriedad simplificada del curso no debe usarse como fuente segura en aplicaciones con valor económico.

**Captura pendiente:** `capturas/cryptozombies-04.png`.
Pie previsto: «Figura 4. Lección 4 completada: combates y actualización del estado de los zombis».

### Lección 5 · ERC721 & Crypto-Collectibles

Se implementa la propiedad y transferencia de zombis como objetos coleccionables. Se estudian funciones y eventos de ERC721, autorizaciones y operaciones aritméticas comprobadas mediante SafeMath en la versión antigua de Solidity que usa el curso.

**Captura pendiente:** `capturas/cryptozombies-05.png`.
Pie previsto: «Figura 5. Lección 5 completada: ERC721, transferencias y protección aritmética».

### Lección 6 · App Front-ends & Web3.js

Se conecta una interfaz JavaScript con el contrato usando su dirección y ABI. Se realizan lecturas, se envían transacciones y se reciben eventos para actualizar la interfaz; la interacción con Ethereum se hace desde el cliente, no desde el código Solidity.

**Captura pendiente:** `capturas/cryptozombies-06.png`.
Pie previsto: «Figura 6. Lección 6 completada: interfaz web conectada al contrato».

## Parte 3 · Learn Git Branching: Main

La rúbrica pide cuatro bloques, con 4 + 4 + 4 + 5 = 17 niveles. En la versión consultada el tercer bloque aparece como **Moving and Staging Work**; corresponde al grupo `move` que el enunciado denomina Moving Work Around. Verificar los bloques por su contenido y número de niveles.

| Bloque | Qué se practica | Órdenes principales |
|---|---|---|
| Introduction Sequence (4) | Crear commits y ramas; fusionar y reorganizar una rama | `git commit`, `git branch`, `git switch`, `git merge`, `git rebase` |
| Ramping Up (4) | HEAD separado, referencias relativas y deshacer cambios | `git switch --detach`, `HEAD^`, `HEAD~2`, `git branch -f`, `git reset`, `git revert` |
| Moving and Staging Work (4) | Mover commits y elegir qué cambios se incluyen | `git cherry-pick`, `git rebase -i`, `git add`, `git restore` |
| A Mixed Bag (5) | Seleccionar cambios, modificar commits, etiquetar y describir versiones | `git cherry-pick`, `git rebase -i`, `git commit --amend`, `git tag`, `git describe` |

`merge` conserva las historias y puede crear un commit con dos padres. `rebase` vuelve a aplicar los cambios sobre otra base y crea commits con identidades nuevas. `reset` mueve una referencia; `revert` añade un commit que deshace el cambio y es más apropiado cuando hay que conservar el historial compartido.

**Captura pendiente:** `capturas/git-main.png`, donde se vean los cuatro bloques completos. Si no caben legibles, utilizar varias imágenes.
Pie previsto: «Figura 7. Los 17 niveles obligatorios de Main completados».

Se ha preparado la guía de Git incluida en el repositorio con los objetivos y comandos por nivel. Consultar una guía no equivale a haber superado los niveles. En el navegador de revisión la carga del primer nivel no llegó a permitir resolverlo; no hay progreso completado que certificar.

## Parte 4 · Learn Git Branching: Remote

El bloque obligatorio **Push & Pull -- Git Remotes!** tiene ocho niveles. Permite practicar clonación, referencias remotas, descarga de cambios, integración y publicación.

| Orden | Relación con pps-entregas |
|---|---|
| `git clone` | Crear una copia local del repositorio |
| `git fetch origin` | Descargar commits y actualizar `origin/main`, sin integrar por sí solo en la rama local |
| `git pull --ff-only` | Actualizar la rama local si basta un avance directo; si diverge, se detiene |
| `git pull --rebase` | Descargar y volver a aplicar commits locales sobre la base remota, si se ha elegido ese flujo |
| `git push origin main` | Publicar los commits locales en la rama remota |
| `git switch -c actividad-4` | Separar el trabajo antes de proponer su integración |

En el simulador aparece `o/main`; en un repositorio real suele ser `origin/main`. `git fakeTeamwork` es una orden del simulador para representar cambios de compañeros y no funciona en la consola real de Git.

**Captura pendiente:** `capturas/git-remote.png`.
Pie previsto: «Figura 8. Los ocho niveles obligatorios de Remote completados».

## Parte 5 · Análisis del contrato de la lección 1

La fábrica recibe un nombre, obtiene un número que representa el ADN, crea una estructura Zombie, la añade al array persistente y emite un evento. En la versión oficial revisada se usa `pragma solidity >=0.5.0 <0.6.0`; hay versiones históricas del curso con otro pragma, por lo que debe documentarse el que aparezca en la sesión del alumno.

| Elemento | Función en el contrato |
|---|---|
| `pragma solidity` | Restringe las versiones del compilador compatibles; no descarga ni selecciona automáticamente un compilador |
| `contract ZombieFactory` | Agrupa el estado y las operaciones de la fábrica |
| `uint dnaDigits = 16` | Indica la cantidad máxima de cifras decimales del ADN |
| `uint dnaModulus = 10 ** dnaDigits` | Define 10 elevado a 16 para limitar el resultado con módulo |
| `struct Zombie` | Agrupa el nombre (`string`) y ADN (`uint`) de cada zombi |
| `Zombie[] public zombies` | Array dinámico persistente con los zombis creados; genera un getter de lectura por índice |
| `_createZombie` | Función privada que construye la estructura, la almacena y emite el evento |
| `_generateRandomDna` | Función privada de lectura que calcula un hash del nombre y lo reduce módulo dnaModulus |
| `createRandomZombie` | Función pública que recibe el nombre y coordina la creación |
| `keccak256` | Produce un hash de 256 bits a partir de bytes; se convierte a uint para obtener el ADN |
| `event NewZombie` | Registra que se ha creado un zombi y permite que la interfaz lo detecte |

`public` en el array permite leer mediante el getter, no concede una escritura libre desde el exterior. `private` limita las llamadas al código, pero no vuelve confidenciales los datos de una blockchain pública. En Solidity 0.5, `zombies.push(...)` devuelve la nueva longitud y el curso resta uno para obtener el índice; en versiones modernas se calcula el índice por separado.

El nombre de `_generateRandomDna` puede resultar engañoso: un hash del mismo nombre siempre da el mismo resultado. No proporciona aleatoriedad secreta ni garantiza que dos entradas distintas produzcan ADN distinto después del módulo. Por ejemplo, crear dos zombis llamados «Albert» en la primera lección puede producir el mismo ADN. El módulo establece un máximo de 16 cifras, no asegura que el número tenga exactamente 16 dígitos sin ceros iniciales.

## Parte 6 · Lección 5, capítulos 9 a 12: desbordamiento y SafeMath

Un **overflow** sucede cuando una operación supera el máximo que representa el tipo. Un **underflow** sucede cuando queda por debajo de su mínimo. En un entero sin signo de ocho bits, el intervalo es 0–255.

En la versión anterior a 0.8 usada por el curso:

```solidity
uint8 numero = 255;
numero++; // queda 0
```

La aritmética sin comprobaciones vuelve al principio del intervalo: 256 módulo 256 es 0. Del mismo modo, restar uno a un `uint8` con valor 0 da 255. En Solidity 0.8 o superior, el primer ejemplo revierte por defecto; no llega a guardar un resultado 0.

SafeMath proporciona operaciones como `add`, `sub`, `mul` y `div` con comprobaciones. En la implementación del curso, `add` verifica que la suma no sea menor que el primer operando y `sub` comprueba que no se reste una cantidad mayor de la disponible. Si la condición falla se aborta la ejecución; estas comprobaciones evitan que un saldo se convierta silenciosamente en un valor incorrecto.

```solidity
using SafeMath for uint256;
saldo = saldo.add(1);
```

La primera línea permite utilizar las funciones de la biblioteca con la sintaxis de método sobre `uint256`. `saldo.add(1)` equivale conceptualmente a `SafeMath.add(saldo, 1)`. **No cambia el comportamiento de `saldo + 1` ni de `saldo++`**: hay que sustituir las operaciones por las llamadas comprobadas.

Ejemplo propio, para razonar sobre el fallo: un contador antiguo de tipo `uint8` con 255 unidades vuelve a cero al sumar una; si representara existencias o permisos disponibles, la aplicación tomaría decisiones con un dato erróneo. Con una operación comprobada se rechaza la actualización y se conserva el estado previo de esa transacción. Es un ejemplo explicativo, no un contrato desplegado ni una prueba realizada sobre una red real.

## Parte 7 · SafeMath32, SafeMath16 y Solidity 0.8

El contrato utiliza campos de tamaños diferentes: `level` y `readyTime` son `uint32`; `winCount` y `lossCount`, `uint16`. SafeMath para uint256 comprueba un intervalo mucho mayor y no sustituye la comprobación del tipo pequeño. Por eso el curso incorpora las versiones específicas:

```solidity
using SafeMath for uint256;
using SafeMath32 for uint32;
using SafeMath16 for uint16;
```

Por ejemplo, sumar uno a 65535 cabe en uint256, pero no en uint16. Si se comprobara solo la suma grande y después se convirtiera sin validar al tipo pequeño, se podría perder información. Las variantes del curso operan sobre el tamaño apropiado y se utilizan al actualizar niveles, victorias y derrotas.

Desde Solidity 0.8 las operaciones aritméticas normales revierten por defecto ante overflow o underflow, por lo que SafeMath ya no hace falta para esa protección básica. Existe `unchecked` para solicitar deliberadamente el comportamiento modular anterior:

```solidity
uint8 numero = 255;
unchecked { numero++; } // en Solidity 0.8: queda 0
```

Esto no significa que Solidity 0.8 elimine todos los riesgos numéricos. Las conversiones explícitas a tipos más estrechos pueden truncar valores; hay que validar el rango antes de convertir. También siguen existiendo errores de lógica y de autorización que SafeMath nunca solucionó. El código del curso no se migra a 0.8 cambiando únicamente el pragma: pueden cambiar otras reglas y APIs del lenguaje.

Fuente: [Solidity, checked/unchecked arithmetic](https://docs.soliditylang.org/en/v0.8.0/control-structures.html#checked-or-unchecked-arithmetic) y [tipos y conversiones](https://docs.soliditylang.org/en/latest/types.html#conversions-between-elementary-types).

## Conclusión

El modelo de ejecución condiciona la seguridad: Ethereum requiere resultados reproducibles y limita los recursos mediante gas, mientras que los programas locales dependen del proceso y el sistema operativo. La protección frente al desbordamiento depende de la versión de Solidity y del tipo utilizado. Git permite conservar y revisar los cambios del proyecto, pero sus simulaciones deben completarse y documentarse con evidencias reales antes de dar por terminada la actividad.

## Bibliografía

- Enunciado ACT_UT1_4 · Solidity + Git, versión revisada de noviembre de 2026, aportado en la conversación.
- Ethereum.org. [Ethereum Virtual Machine](https://ethereum.org/developers/docs/evm/) y [Gas and fees](https://ethereum.org/developers/docs/gas/).
- CryptoZombies. [Curso Solidity](https://cryptozombies.io/solidity) y [fuentes oficiales de las lecciones](https://github.com/CryptozombiesHQ/cryptozombie-lessons), lecciones 1 y 5.
- Solidity. [Control structures, versión 0.8.0](https://docs.soliditylang.org/en/v0.8.0/control-structures.html) y [Types](https://docs.soliditylang.org/en/latest/types.html).
- Learn Git Branching. [Simulador](https://learngitbranching.js.org/) y [código fuente oficial](https://github.com/pcottle/learnGitBranching).
