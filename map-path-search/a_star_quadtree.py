# import queue
import math
from heapq import heappush, heappop
from utils_custom import dist2d
import quadtreemap


def _get_movements_4n(qtm, tile):
    neighborList = []
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0 - 1, tile.boundary.y0,
                                                                           tile.boundary.width + 2,
                                                                           tile.boundary.height)))
    neighborList.append(qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0, tile.boundary.y0 - 1,
                                                                           tile.boundary.width,
                                                                           tile.boundary.height + 2)))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def _get_movements_8n(qtm: quadtreemap.QuadTreeMap, tile: quadtreemap.Tile):
    neighborList = qtm.quadtree.tileIntersect(quadtreemap.BoundingBox(tile.boundary.x0 - 1, tile.boundary.y0 - 1,
                                                                      tile.boundary.width + 2,
                                                                      tile.boundary.height + 2))
    movements = [(til, quadtreemap.Point.disOf2Points(tile.getCenter(), til.getCenter())) for til in neighborList]
    return movements


def a_star_quadtree(start_m, goal_m, qtm, movement='8n', occupancy_cost_factor=3):
    path_record = {}
    # candidates = queue.PriorityQueue()

    # get array indices of start and goal
    start = qtm.quadtree.searchTileByIdx(quadtreemap.Point(start_m[0], start_m[1]))
    goal = qtm.quadtree.searchTileByIdx(quadtreemap.Point(goal_m[0], goal_m[1]))

    # check if start and goal nodes correspond to free spaces
    if not start or start.tile_points:
        raise Exception('Start node is not traversable')
    if not goal or goal.tile_points:
        raise Exception('Goal node is not traversable')

    # Heuristics definition
    start_node_cost = 0
    start_node_estimated_cost_to_goal = quadtreemap.Point.disOf2Points(start.getCenter(), goal.getCenter()) + start_node_cost
    # print(start_node_estimated_cost_to_goal)
    front = [(start_node_estimated_cost_to_goal, start_node_cost, start, None)]

    # candidates.put((0, None, start))  # store (distance, previous-tile, current-tile)
    # came_from = {}

    while front:
        element = heappop(front)

        total_cost, dis, curr_node, prev_node = element

        # print(curr_node, "\t", goal)
        if curr_node == goal:
            # print(True)
            path_record[curr_node] = prev_node
            break
        if curr_node in path_record:
            continue
        path_record[curr_node] = prev_node

        # get possible movements

        if movement == '4N':
            movements = _get_movements_4n(qtm, curr_node)
        elif movement == '8N':
            movements = _get_movements_8n(qtm, curr_node)
        else:
            raise ValueError('Unknown movement')


        # qtm.mark_visited_idx(prev_node)

        # check all neighbors
        for til, deltacost in movements:
            # check whether new position is inside the map or is an obstacle
            # if not, skip node
            if til.tile_points:
                continue
            if til not in path_record:
                x_index = int(round(til.getCenter().x/qtm.cell_size))
                y_index = int(round(til.getCenter().y/qtm.cell_size))
                potential_function_cost = qtm.data[y_index][x_index] * occupancy_cost_factor
                new_cost = dis + deltacost + potential_function_cost
                new_total_cost_to_goal = new_cost + quadtreemap.Point.disOf2Points(til.getCenter(), goal.getCenter()) + potential_function_cost

                heappush(front, (new_total_cost_to_goal, new_cost, til, curr_node))
    # reconstruct path backwards (only if we reached the goal)
    path = []
    path_idx = []
    # print(len(path_record))
    # print(path_record)
    if goal in path_record:
        node = goal
        while node:
            path_idx.append(node)
            # transform array indices to meters
            # node_m_x, node_m_y = gmap.get_coordinates_from_index(node[0], node[1])
            # path.append((node_m_x, node_m_y))
            node = path_record[node]
        # reverse so that path is from start to goal.
        path.reverse()
        path_idx.reverse()

    # print("path_idx len: ", len(path_idx))
    # print("path_idx:\n", path_idx)
    return path, path_idx
