PLOT_PATH = ../../../tools/plots
DATA_PATH = ../data
IMAGE_PATH = ../images
MEASUREMENT_PATH = -I ~/Desktop/codes/measurements/include
CXX = g++
CXXFLAGS = -g -Wall --pedantic -fno-elide-constructors -std=c++20 -O3


clean: 
	rm -f main ../data/*/c.dat 

main: main.cpp
	$(CXX) $(CXXFLAGS) $(MEASUREMENT_PATH) -o $@ $< 

plot_CW:
	python3 $(PLOT_PATH)/measurements_error_bars.py $(DATA_PATH)/CW.txt $(IMAGE_PATH)/CW.png \
			'Misure metodo CW' 'n° di misura' 'c [m/s]'  

plot_CCW:
	python3 $(PLOT_PATH)/measurements_error_bars.py $(DATA_PATH)/CCW.txt $(IMAGE_PATH)/CCW.png \
			'Misure metodo CCW' 'n° di misura' 'c [m/s]'  

plot_CW_CCW:
	python3 $(PLOT_PATH)/measurements_error_bars.py $(DATA_PATH)/CW_CCW.txt $(IMAGE_PATH)/CW_CCW.png \
			'Misure metodo CW-CCW' 'n° di misura' 'c [m/s]'  

plot_results: 
	python3 $(PLOT_PATH)/measurements_error_bars.py $(DATA_PATH)/c_values.txt $(IMAGE_PATH)/results.png \
			'Misure velocità della luce' 'n° di misura' 'c [m/s]'  

plot_all: plot_CW plot_CCW plot_CW_CCW plot_results

clear_images:
	rm $(IMAGE_PATH)/*.png